from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(null=False, blank=False)
    image2 = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=40)
    text = models.TextField()
    text2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
