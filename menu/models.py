from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='category')
    name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=250)

    def __str__(self):
        return str(self.title)
