from django.http import JsonResponse
from django.shortcuts import render
from .models import Categories
# from .utils.db_utils import get_connection
from .utils.db_utils import fetch_orders_with_details_raw
# Create your views here.

def orders_with_details_api(request):
    """
    API endpoint that returns every joined Order+Detail+Customer+Product row.
    """
    data = fetch_orders_with_details_raw()
    return JsonResponse(data, safe=False)

def home(request):
    return render(request,'databasefapp/home.html')

def ShowCategories(request):
    categories = Categories.objects.all()

    return render(request,'databasefapp/showCategories.html',{'Categories':categories})