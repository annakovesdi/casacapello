# Generated by Django 4.1.8 on 2023-04-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0003_wines_price2'),
    ]

    operations = [
        migrations.AddField(
            model_name='wines',
            name='imagebanner',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
