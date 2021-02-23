from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return HttpResponse("Tech with tim!")

def v1(response):
        return HttpResponse("View 1")

def register(request):
    form = UserCreationForm()
    return render(request,'main/register.html',{'form': form})
