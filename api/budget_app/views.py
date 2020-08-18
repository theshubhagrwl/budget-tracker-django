from re import search
from api.users.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Items
import json
from django.core.exceptions import ObjectDoesNotExist


class UserItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    perimission_classes = [IsAuthenticated]
    # queryset = Items.objects.all()

    def get_queryset(self,  *args):
        return Items.objects.filter(user=self.request.user.id)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated]


@csrf_exempt
@api_view(['POST', ])
def addItem(request):
    # user = request.user
    item = Items(user=request.user)
    if request.method == "POST":
        serializer = ItemSerializer(item, data=request.data)
        # data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # try:
    #     # author = User.objects.get(id=payload["user"])
    #     item = Items.objects.create(
    #         title=payload["title"],
    #         description=payload["description"],
    #         user=user,
    #     )
    #     serializer = ItemSerializer(item)
    #     return JsonResponse({'books': serializer.data})
    # except ObjectDoesNotExist as e:
    #     return JsonResponse({'error': str(e)})
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible went wrong'})

# @csrf_exempt
# @api_view(['GET', "POST"])
# def add_item(request):
#     if request.method == 'POST':
#         data = request.POST
#         user = request.user

#         return JsonResponse({"data": data})

#     return JsonResponse({"data": "data will show here"})
# def home(request):
#     return render(request, 'budget_app/home.html', {'home_page': 'active'})


# @login_required
# def items(request):
#     if request.method == 'GET':
#         # ordering items by date
#         ordered_items = BudgetItem.objects.filter(
#             user=request.user).order_by('-date')
#         # to calculate the total amount of duplicate values
#         dups = BudgetItem.objects.filter(user=request.user).values(
#             'title').annotate(Sum('amount'))
#         return render(request, 'budget_app/items.html', {'items': ordered_items, 'item_page': 'active', 'dups': dups, 'form': MonthForm()})
#     else:
#         form = MonthForm(request.POST)
#         data = request.POST.copy()
#         # month = form.save(commit=False)
#         month = data.get('month_number')
#         print(month)
#         items = BudgetItem.objects.filter(
#             user=request.user).filter(date__month=month)
#         dups = BudgetItem.objects.filter(user=request.user).filter(date__month=month).values(
#             'title').annotate(Sum('amount'))
#         return render(request, 'budget_app/items.html', {'items': items, 'dups': dups})


# def signupuser(request):
#     if request.method == "GET":
#         return render(request, 'budget_app/signup.html', {'form': SignupForm()})
#     else:
#         # Create new user
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(
#                     request.POST['username'], request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('home')
#             except IntegrityError:
#                 return render(request, 'budget_app/signup.html', {'form': SignupForm(), 'error': 'username taken'})

#         else:
#             # Tell pass didn't match
#             return render(request, 'budget_app/signup.html', {'form': SignupForm(), 'error': 'pass did not match'})


# @login_required
# def logoutuser(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect(home)


# def loginuser(request):
#     if request.method == 'GET':
#         return render(request, 'budget_app/login.html', {'form': LoginForm()})
#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user == None:
#             return render(request, 'budget_app/login.html', {'form': LoginForm(), 'error': 'Username and password did not match'})
#         else:
#             login(request, user)
#             return redirect(home)


# @login_required
# def addItem(request):
#     if request.method == "GET":
#         return render(request, 'budget_app/addItem.html', {'form': addItemForm()})
#     else:
#         form = addItemForm(request.POST)
#         newItem = form.save(commit=False)
#         newItem.user = request.user
#         # converting to lowercase to assist in count function
#         newItem.title = newItem.title.lower()
#         newItem.save()
#         return redirect(items)


# def about(request):
#     return render(request, 'budget_app/about.html', {'about_page': 'active'})


# @login_required
# def updateItem(request, pk):
#     u_items = BudgetItem.objects.filter(user=request.user).get(id=pk)
#     form = addItemForm(instance=u_items)

#     if request.method == "POST":
#         form = addItemForm(request.POST, instance=u_items)
#         form.save()
#         return redirect(items)

#     return render(request, 'budget_app/updateItem.html', {'items': u_items, 'form': form})


# @login_required
# def deleteItem(request, pk):
#     item = BudgetItem.objects.filter(user=request.user).get(id=pk)

#     if request.method == 'POST':
#         item.delete()
#         return redirect(items)

#     return render(request, 'budget_app/deleteItem.html', {'item': item})
