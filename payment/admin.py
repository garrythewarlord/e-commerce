from django.contrib import admin

from .models import Order, OrderItem, PendingOrder

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PendingOrder)