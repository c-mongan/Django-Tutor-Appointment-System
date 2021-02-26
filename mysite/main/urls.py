# urls.py
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views




from . import views

urlpatterns = [
    path('', views.BookingListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('v1/', views.v1, name='view 1'),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('booking/<int:pk>/update/', views.BookingUpdateView.as_view(), name='booking-update'),
    path('booking/new/', views.BookingCreateView.as_view(), name='booking-create'),
    path('booking/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking-delete'),

]
