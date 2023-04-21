# Generated by Django 4.1.8 on 2023-04-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0004_reservation_email_address_reservation_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='datetime',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]