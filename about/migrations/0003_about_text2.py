# Generated by Django 4.1.4 on 2023-04-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='text2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
