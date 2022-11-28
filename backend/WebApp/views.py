from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader
from WebApp.models import User, Admin_User
from WebApp.serializers import User_Serializer, Admin_Serializer
from rest_framework import viewsets

# Admin website.
def index(request):
    template = loader.get_template("./index.html")
    ls = []
    for n in range(11):
        ls.append(1)
    context = {
        "ln": ls
    }
    return HttpResponse(template.render(context, request))

# Api Classes and Configuration.