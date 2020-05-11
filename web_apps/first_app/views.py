from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1 align=center>Hello world.This is my first Django Application.</h1>")