# urls.py
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views




from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('v1/', views.v1, name='view 1'),
    path('login/',auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
]
