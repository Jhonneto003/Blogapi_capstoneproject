from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer,UserSerializer

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model=CustomUser
        fields=['id','email','username', 'first_name','last_name']


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=CustomUser
        fields=['id', 'username', 'email', 'first_name','last_name', 'password','date_of_birth', 'date_joined']



        