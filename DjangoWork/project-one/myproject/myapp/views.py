from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello world! Django app created")

def farhan(request):
    return HttpResponse("<h1>Hello world! Django app created BY FARHAN WASEER")