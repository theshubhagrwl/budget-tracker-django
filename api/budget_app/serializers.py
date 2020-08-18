from rest_framework import serializers
from .models import Items


# class ItemSerializer(serializers.HyperlinkedModelSerializer):
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ("__all__")
