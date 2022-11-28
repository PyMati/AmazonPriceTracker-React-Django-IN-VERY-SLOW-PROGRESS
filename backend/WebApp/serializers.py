from rest_framework import serializers
from WebApp.models import User, Admin_User


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        

class Admin_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_User
        fields = ("username", "password")