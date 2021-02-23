# urls.py
from django.urls import path


from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('v1/', views.v1, name='view 1'),
    path('register/',views.register, name='register'),
]
