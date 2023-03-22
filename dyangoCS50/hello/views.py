from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def david(request):
    return HttpResponse("Hello, David")


def joy(request):
    return HttpResponse("Hello, Joy")


def greet(request, name):
    return render(request, "hello/greeting.html", {
        "name": name.capitalize()
    })
