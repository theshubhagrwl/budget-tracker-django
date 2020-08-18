# from django import forms
# from django.forms import ModelForm
# from .models import BudgetItem
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class DateInput(forms.DateInput):
#     input_type = 'date'


# class addItemForm(ModelForm):
#     class Meta:
#         model = BudgetItem
#         fields = ['title', 'amount', 'date']
#         widgets = {
#             'date': DateInput(),
#         }
#     title = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Item Name',
#         }
#     ))
#     amount = forms.DecimalField(widget=forms.NumberInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter amount',
#         }
#     ))
#     date = forms.CharField(widget=DateInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter date',
#         }
#     ))


# class SignupForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your username',
#         }
#     ))
#     password1 = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter password',
#         }
#     ))
#     password2 = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'Retype password',
#         }
#     ))


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control col-6',
#             'placeholder': 'Enter your username',
#         }
#     ))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control col-6',
#             'placeholder': 'Enter password',
#         }
#     ))


# CHOICES = (
#     ("1", "Jan"),
#     ("2", "Feb"),
#     ("3", "Mach"),
#     ("4", "April"),
#     ("5", "May"),
#     ("5", "June"),
#     ("5", "July"),
#     ("5", "August"),
#     ("5", "September"),
#     ("5", "October"),
#     ("5", "November"),
#     ("5", "December"),
# )


# class MonthForm(forms.Form):
#     month_number = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
#         attrs={
#             'class': 'form-control col-6 mx-auto',
#             'onChange': 'this.form.submit()',
#         }
#     ))
