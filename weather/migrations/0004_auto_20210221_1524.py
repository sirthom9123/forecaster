# Generated by Django 3.1.7 on 2021-02-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20210220_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='humidity',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='wind',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]