from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'friendly_name',
        'cat_image',
    )


admin.site.register(Category, CategoryAdmin)
