# Generated by Django 3.0.7 on 2020-06-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0005_auto_20200611_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='data',
            field=models.DateTimeField(default=''),
        ),
    ]
