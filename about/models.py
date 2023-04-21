from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(null=False, blank=False,
                              verbose_name='About Us Image')
    imagebanner = models.ImageField(null=True, blank=True,
                                    verbose_name='About Us page banner image')
    title = models.CharField(max_length=40)
    text = models.TextField()
    text2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)
