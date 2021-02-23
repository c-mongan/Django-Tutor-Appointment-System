from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #for flash messages


def index(request):
    return HttpResponse("Tech with tim!")

def v1(response):
        return HttpResponse("View 1")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #If it recieves a post request it means an account is being created
        if form.is_valid():
            username = form.cleaned_data.get('username') #If the username follows the condition it is allowed
            messages.success(request,f'Account created for {username}!') #f string ---> this line is flash message
            return redirect('index')

    else:
     form = UserCreationForm()
    return render(request,'main/register.html',{'form': form})
