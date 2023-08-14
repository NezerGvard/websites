from django.contrib import admin
from .models import *

class PrototypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'context', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'address')
    list_display_links = ('id', 'address')
    search_fields = ('id', 'total_price', 'byt_at')

admin.site.register(Product, PrototypeAdmin)

admin.site.register(Order, OrderAdmin)
