from django.contrib import admin

from .models import Categories, Customers, DjangoSession, Employees, OrderDetails, Orders, Products, Shippers, Suppliers

# Register your models here.
admin.site.register(Suppliers)
admin.site.register(Shippers)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Employees)
admin.site.register(DjangoSession)
admin.site.register(Customers)
admin.site.register(Categories)




