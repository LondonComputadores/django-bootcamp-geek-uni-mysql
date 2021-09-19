from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'storage', 'slug', 
                                'created_at', 'modified_at', 'active')
