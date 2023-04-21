from django.contrib import admin
from .models import Category, Wines, BannerImage


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



class BannerImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )    


admin.site.register(Wines, WinesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
