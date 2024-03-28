from django.urls import path
from django.shortcuts import render


def homePage(request):
    return render(request, 'home.html')