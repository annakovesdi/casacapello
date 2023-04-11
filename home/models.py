from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=254)

    def __str__(self):
        return str(self.title)
