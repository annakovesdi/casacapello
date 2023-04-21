from django.contrib import admin
from .models import Category, Menu, BannerImage


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


class BannerImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
