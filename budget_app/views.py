from budget_app.serializers import BudgetItemSerializer
from django.shortcuts import render, redirect
from rest_framework import request
# from django.contrib.auth.models import User
from users.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import addItemForm, SignupForm, LoginForm, MonthForm
from .models import BudgetItem
from django.views.generic.base import TemplateView
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', "POST"])
def hello(request):
    return Response({"Hello": 'World'})


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetItemSerializer
    queryset = BudgetItem.objects.all()
    permission_classes = [IsAuthenticated]


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
