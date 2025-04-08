from django.shortcuts import render
from .models import Categories
# Create your views here.



def home(request):
    return render(request,'databasefapp/home.html')

def ShowCategories(request):
    categories = Categories.objects.all()

    return render(request,'databasefapp/showCategories.html',{'Categories':categories})