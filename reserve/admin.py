from django.contrib import admin
from .models import Reservation, BannerImage


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'persons',
        'date',
        'time',
        'email_address',
        'reserved_time',
    )


class BannerImageAdmin(admin.ModelAdmin):
    list_display = (
        'image',
    )


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(BannerImage, BannerImageAdmin)
