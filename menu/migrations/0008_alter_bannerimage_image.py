# Generated by Django 4.1.8 on 2023-04-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_bannerimage_remove_category_imagebanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Change banner image menupage'),
        ),
    ]
