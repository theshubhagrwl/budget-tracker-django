from rest_framework import serializers
from .models import BudgetItem


class BudgetItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetItem
        fields = ("__all__")
