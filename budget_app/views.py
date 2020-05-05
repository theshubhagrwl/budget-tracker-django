from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'budget_app/home.html')


def signupuser(request):
    if request.method == "GET":
        return render(request, 'budget_app/signup.html', {'form': UserCreationForm()})
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
                return render(request, 'budget_app/signup.html', {'form': UserCreationForm(), 'error': 'username taken'})

        else:
            # Tell pass didn't match
            return render(request, 'budget_app/signup.html', {'form': UserCreationForm(), 'error': 'pass did not match'})


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'budget_app/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user == None:
            return render(request, 'budget_app/login.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect(home)
