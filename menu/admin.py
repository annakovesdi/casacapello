from django.contrib import admin
from .models import Category, Menu


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'description',
        'hide',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
