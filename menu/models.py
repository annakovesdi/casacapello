from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.name)


class Menu(models.Model):
    category = models.ForeignKey(
        'Category', null=False, blank=False,
        on_delete=models.RESTRICT, related_name='category')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=250)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
