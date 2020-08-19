from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # for attr, value in validated_data:
        #     if attr == 'password':
        #         instance.set_password(value)
        #     else:
        #         setattr(instance, attr, value)
        # for attr, value in validated_data:
        #     if attr == 'name':
        #         instance.set_name(value)
        #     else:
        #         setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ("id", 'name', 'email', 'password',
                  'is_active', 'is_staff', 'is_superuser')
        # fields = ('name', 'email', 'password',
        #           'active', 'is_staff', 'admin')
