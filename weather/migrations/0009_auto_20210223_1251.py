# Generated by Django 3.1.7 on 2021-02-23 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0008_apikey'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apikey',
            old_name='map_api',
            new_name='api_key',
        ),
        migrations.RenameField(
            model_name='apikey',
            old_name='weather_api',
            new_name='name',
        ),
    ]
