# Generated by Django 3.0.7 on 2020-06-11 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0010_auto_20200611_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='data',
        ),
    ]