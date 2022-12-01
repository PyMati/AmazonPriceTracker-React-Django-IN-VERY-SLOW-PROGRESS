from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from WebApp.models import User, Admin_User, Worker_Data
from WebApp.serializers import User_Serializer, Admin_Serializer, Worker_Data_Serializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Admin website.
def index(request):
    template = loader.get_template("./index.html")
    dataset = User.objects.all()
    context = {
        "users": dataset
    }
    
    return HttpResponse(template.render(context, request))

# Api configuration.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin_User.objects.all()
    serializer_class = Admin_Serializer


class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Worker_Data.objects.all()
    serializer_class = Worker_Data_Serializer
    
    
@api_view(["POST"])
def saveUser(request):
    serializer = User_Serializer(data = request.data)
    print(request.data)
    if serializer.is_valid():
        user = serializer.save()
        
    data = User_Serializer(User.objects.all(), many = True)
    return Response({"data": data.data})

@api_view(["GET"])
def showUsers(request):
    return Response(User.objects.all())