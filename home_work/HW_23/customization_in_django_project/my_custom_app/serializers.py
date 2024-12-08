from rest_framework import serializers
from .models import MyModel
from django.contrib.auth.models import User


class MyModelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description', 'user', 'related_model']  # Поля, которые будут возвращаться в API
