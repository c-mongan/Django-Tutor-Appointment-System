from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages #for flash messages
from .forms import UserRegisterForm
from .models import Booking
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.models import User

from bootstrap_datepicker_plus import DateTimePickerInput


def index(request):
    context = {
        'posts':Booking.objects.all()# will be changed to booking
    }
    return render (request,'main/home.html',context)

def about(request):
     return render (request,'main/about.html',{'title':'About'})

class BookingListView(ListView):
    model = Booking
    template_name = 'main/home.html'
    context_object_name = 'posts' #will be changed to booking
    ordering = ['-date_posted']
    paginate_by = 5 #how many bookings per page

class UserBookingListView(ListView):
    model = Booking
    template_name = 'main/mybookings.html'
    context_object_name = 'posts' #will be changed to booking
    paginate_by = 5 #how many bookings per page
 
    def get_queryset(self):
     user = get_object_or_404(User,username =self.kwargs.get('username'))
     return Booking.objects.filter(author=user).order_by('-date_posted')



class BookingDetailView(DetailView):
    model = Booking

class BookingCreateView(LoginRequiredMixin,CreateView):
    model = Booking
    fields = ['title','content', 'details','datetime']
    
    def form_valid(self,form):

     form.instance.author = self.request.user #set booking creator as current logged in user
     form.fields['datetime'].widget = DateTimePickerInput()
     return super().form_valid(form)

    
 
class BookingUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Booking
    fields = ['title','content','details','datetime']
    
    def form_valid(self,form):
     form.instance.author = self.request.user #set booking creator as current logged in user
     form.fields['datetime'].widget = DateTimePickerInput()
     return super().form_valid(form)

    def test_func(self): #users cant edit other users bookings (NEEDS TO BE TESTED)
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
 
class BookingDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Booking
    success_url = '/'
    
    def test_func(self): #users cant delete other users bookings (NEEDS TO BE TESTED)
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
   

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) #If it recieves a post request it means an account is being created
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #If the username follows the condition it is allowed
            messages.success(request,f'Account created for {username} Please log in!') #f string ---> this line is flash message
            return redirect('login')

    else:
     form = UserRegisterForm()
    return render(request,'main/register.html',{'form': form})

@login_required()
def profile(request):
    return render(request, 'main/profile.html')