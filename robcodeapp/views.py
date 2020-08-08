from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"robcodeapp/home.html")

def services(request):
    return render(request,"robcodeapp/services.html")

def aboutus(request):
    return render(request,"robcodeapp/aboutus.html")

def contactus(request):
    return render(request,"robcodeapp/contactus.html")

