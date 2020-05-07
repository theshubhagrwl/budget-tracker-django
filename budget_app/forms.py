from django import forms
from django.forms import ModelForm
from .models import BudgetItem
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class DateInput(forms.DateInput):
    input_type = 'date'


# class ShowDateWiseData(ModelForm):
#     month = forms.DateField()


class addItemForm(ModelForm):
    class Meta:
        model = BudgetItem
        fields = ['title', 'amount', 'date']
        widgets = {
            'date': DateInput(),
        }
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Item Name',
            'text-transform': 'lowercase',
        }
    ))
    amount = forms.DecimalField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter amount',
        }
    ))
    date = forms.CharField(widget=DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter date',
        }
    ))


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter password',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Retype password',
        }
    ))
    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'form-control'
    #     }
    # ))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control col-6',
            'placeholder': 'Enter your username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control col-6',
            'placeholder': 'Enter password',
        }
    ))
