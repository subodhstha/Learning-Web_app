from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("Hello!")

def index(request):
    return render(request, "hello/index.html")


def world(request):
    return HttpResponse("Hello, world!")

def python(request):
    return HttpResponse("Hello, Python!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })