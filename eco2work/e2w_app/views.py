from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello from eco2work  index')


def edit(request):
    return HttpResponse('Hello from eco2work  edit')
