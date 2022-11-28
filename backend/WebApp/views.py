from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("./ASite.html")
    ls = []
    for n in range(11):
        ls.append(1)
    context = {
        "ln": ls
    }
    return HttpResponse(template.render(context, request))