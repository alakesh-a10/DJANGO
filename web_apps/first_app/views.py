from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={'insert_me':'This line is printed from Views.py'}
    return render(request,'first_app/index.html',context=my_dict)
    return HttpResponse("<h1 align=center>Hello world.This is my first Django Application.</h1>")