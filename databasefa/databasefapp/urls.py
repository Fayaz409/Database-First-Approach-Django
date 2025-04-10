from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('categories/',views.ShowCategories,name='Categories'),
    path(
        'orders_with_details_api/',
        views.orders_with_details_api,
        name='orders_with_details_api'
    ),
]
