from django.contrib import admin
from .models import Home


class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Home, HomeAdmin)