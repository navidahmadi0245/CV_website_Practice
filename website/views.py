from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def http_test(request):
    return HttpResponse("hello")
