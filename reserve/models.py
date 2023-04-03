from django.db import models


class Reserve(models.Model):
    name = models.CharField(max_length=254)
    datetime = models.DateTimeField()
    reserved_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
