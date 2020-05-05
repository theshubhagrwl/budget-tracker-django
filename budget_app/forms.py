from django import forms
from django.forms import ModelForm
from .models import BudgetItem


class DateInput(forms.DateInput):
    input_type = 'date'


class addItemForm(ModelForm):
    class Meta:
        model = BudgetItem
        fields = ['title', 'description', 'amount', 'date']
        widgets = {
            'date': DateInput(),
        }
