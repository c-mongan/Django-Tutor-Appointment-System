from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages #for flash messages
from .forms import UserRegisterForm
from .models import Booking


def index(request):
    context = {
        'posts':Booking.objects.all()#dictionary
    }
    return render (request,'main/home.html',context)

def about(request):
     return render (request,'main/about.html',{'title':'About'})


def v1(response):
        return HttpResponse("View 1")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) #If it recieves a post request it means an account is being created
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #If the username follows the condition it is allowed
            messages.success(request,f'Account created for {username}!') #f string ---> this line is flash message
            return redirect('index')

    else:
     form = UserRegisterForm()
    return render(request,'main/register.html',{'form': form})
