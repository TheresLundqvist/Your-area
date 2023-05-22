from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'rating',
        'image',
        'category',
    )

    ordering = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
