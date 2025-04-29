from django.contrib import admin
from .models import Category, Brand, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'created_at')


admin.site.register(Category, CategoryAdmin),
admin.site.register(Brand, BrandAdmin),
admin.site.register(Product, ProductAdmin)
