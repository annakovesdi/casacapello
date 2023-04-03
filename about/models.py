from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=40)
    text = models.TextField()

    def __str__(self):
        return str(self.title)
