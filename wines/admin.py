from django.contrib import admin
from .models import Category, Wines


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class WinesAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'price',
        'description',
        'hide',
    )


admin.site.register(Wines, WinesAdmin)
admin.site.register(Category, CategoryAdmin)
