from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils import timezone


class Reservation_Date(models.Model):
    date = models.DateField()
    is_full = models.BooleanField()

    def __str__(self):
       return self.date


class Reservation(models.Model):
    # reservation_date = models.ForeignKey(Reservation_Date, on_delete=models.CASCADE, default=1, null=True)
    name = models.CharField(max_length=254)
    persons = models.IntegerField(validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ])
    date = models.CharField(max_length=10)
    time = models.DateTimeField()
    reserved_time = models.DateTimeField(auto_now=True)
    email_address = models.CharField(max_length=254)
    phone = models.IntegerField(validators=[
            MinValueValidator(10)
        ])

    def __str__(self):
        return str(self.name)


class BannerImage(models.Model):
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Change banner image reservation page')
