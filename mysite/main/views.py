from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #for flash messages

posts = [
    {  #bookings

'author':'Conor', #Student name
'title': 'Booking 1', #Booking ID
'content':'Spanish', #Subject
'date_posted': 'August 27th 2020'#Date booked
    },
{
'author':'Andrew', #Student name
'title': 'Booking 2', #Booking ID
'content':'Math', #Subject
'date_posted': 'December 17th 2020'#Date booked


}
]
def index(request):
    context = {
        'posts':posts #dictionary
    }
    return render (request,'main/home.html',context)

def about(request):
     return render (request,'main/about.html',{'title':'About'})


def v1(response):
        return HttpResponse("View 1")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) #If it recieves a post request it means an account is being created
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #If the username follows the condition it is allowed
            messages.success(request,f'Account created for {username}!') #f string ---> this line is flash message
            return redirect('index')

    else:
     form = UserCreationForm()
    return render(request,'main/register.html',{'form': form})
