from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import addItemForm, SignupForm, LoginForm
from .models import BudgetItem
from django.views.generic.base import TemplateView
from django.db.models import Sum


def home(request):
    return render(request, 'budget_app/home.html', {'home_page': 'active'})


def items(request):
    items = BudgetItem.objects.filter(user=request.user)
    # to calculate the total amount of duplicate values
    dups = items.values('title').annotate(Sum('amount'))
    # print(dups)
    return render(request, 'budget_app/items.html', {'items': items, 'item_page': 'active', 'dups': dups})

# class ItemView(TemplateView):
#     template_name = 'budget_app/items.html'

#     def get_context_data(self, **kwargs):
#         items = super().get_context_data(**kwargs)
#         items['items'] = BudgetItem.objects.filter(user=self.user)
#         return items


def signupuser(request):
    if request.method == "GET":
        # return render(request, 'budget_app/signup.html', {'form': UserCreationForm()})
        return render(request, 'budget_app/signup.html', {'form': SignupForm()})
    else:
        # Create new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'budget_app/signup.html', {'form': SignupForm(), 'error': 'username taken'})

        else:
            # Tell pass didn't match
            return render(request, 'budget_app/signup.html', {'form': SignupForm(), 'error': 'pass did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'budget_app/login.html', {'form': LoginForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'budget_app/login.html', {'form': LoginForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect(home)


def addItem(request):
    if request.method == "GET":
        return render(request, 'budget_app/addItem.html', {'form': addItemForm()})
    else:
        form = addItemForm(request.POST)
        newItem = form.save(commit=False)
        newItem.user = request.user
        newItem.save()
        return redirect(items)


def about(request):
    return render(request, 'budget_app/about.html', {'about_page': 'active'})
