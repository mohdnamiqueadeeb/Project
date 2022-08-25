from django.shortcuts import render
from django.http import request
from django.shortcuts import render, HttpResponsePermanentRedirect

# Create your views here.


def show(request):
    return render(request, 'home.html')


def loginpage(request):
    return render(request, 'login.html')


def registerpage(request):
    return render(request, 'register.html')
