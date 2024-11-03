from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse("Welcome to main page")

def about_view(request):
    return HttpResponse("about us page")

def contact_view(request):
    return HttpResponse("contact to us")