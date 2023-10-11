
from django.urls import path

from . import views

urlpatterns = [

    path('',views.demo,name='demo'),
    path('', views.obj,name='obj'),
    path('home/',views.home,name='home'),
    path('add/', views.addition,name='addition'),
]