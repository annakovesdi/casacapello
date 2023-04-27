from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils import timezone


class Reservation_Date(models.Model):
    date = models.DateField()
    is_Full = models.BooleanField()


class Reservation(models.Model):
    reservation_date = models.ForeignKey(relatedField='date')
    name = models.CharField(max_length=254)
    persons = models.IntegerField(validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ])
    date = models.CharField(null=True, blank=True, max_length=10)
    time = models.DateTimeField(null=True, blank=True)
    reserved_time = models.DateTimeField(auto_now=True)
    email_address = models.CharField(max_length=254, null=True, blank=True)
    phone = models.IntegerField(validators=[
            MinValueValidator(10)
        ], null=True, blank=True)

    def __str__(self):
        return str(self.name)


class BannerImage(models.Model):
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Change banner image reservation page')
