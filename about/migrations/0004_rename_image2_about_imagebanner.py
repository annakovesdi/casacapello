# Generated by Django 4.1.8 on 2023-04-17 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_text2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image2',
            new_name='imagebanner',
        ),
    ]
