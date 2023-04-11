from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'text'
    )


admin.site.register(About, AboutAdmin)