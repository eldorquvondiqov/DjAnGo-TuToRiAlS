from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('<h1>Hello World!</h1> <br> <h2> Eldor </h2>')