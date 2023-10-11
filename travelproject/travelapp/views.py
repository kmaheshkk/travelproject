from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from  .models import Animal
# Create your views here.
def demo (request):
    obj=Place.objects.all()

    return render(request,"index.html",{'result':obj})
def obj(request):

    obj1 = Animal.objects.all()
    return render(request,"index.html",{'result1':obj1})
def home(request):
    return render(request,'home.html')
def addition(request):
    x=int(request.GET['num1'])
    y = int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{'result':res})


