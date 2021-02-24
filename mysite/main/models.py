from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):

 title = models.CharField(max_length=20) #Booking ID
 content = models.TextField() #Subject
 date_posted= models.DateTimeField(default=timezone.now) #Date booked
 author = models.ForeignKey(User, on_delete=models.CASCADE)#User who booked booking

 def __str__(self): #For declaring how we would like our bookings to be printed - by title
         return self.title