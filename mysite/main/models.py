from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
class Booking(models.Model):

 subject = models.CharField("Subject", max_length=20) #Booking ID
 teacher = models.CharField("Teacher", max_length=20) #Subject
 details = models.TextField("Details", max_length=20, blank=True)
 date_posted= models.DateTimeField(default=timezone.now) #Date booked
 student = models.ForeignKey(User, on_delete=models.CASCADE)#User who booked booking
 datetime = models.DateTimeField("Date & Time",default = timezone.now)

 def __str__(self): #For declaring how we would like our bookings to be printed - by title
         return self.title


 def get_absolute_url(self):
  return reverse('booking-detail', kwargs={'pk': self.pk})

class Teacher(models.Model):
  name = models.CharField("Name", max_length=20) 
  subject = models.CharField("Subject", max_length=20) 

class Slots(models.Model):
        teacherid = models.ForeignKey(Teacher, on_delete=models.CASCADE)
        datetime1 = models.DateTimeField("Date & Time",default = timezone.now)
        datetime2 = models.DateTimeField("Date & Time",default = timezone.now)
        datetime3 = models.DateTimeField("Date & Time",default = timezone.now)
        
