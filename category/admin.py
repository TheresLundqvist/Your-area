from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('friendly_name', 'slug')


admin.site.register(Category, CategoryAdmin)
