from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My second App</em")

''' Task to create a help page'''
def help(request):
    return render(request,'appTwo/help.html')