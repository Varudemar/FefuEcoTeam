# Generated by Django 3.0.7 on 2020-06-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcoApp', '0008_auto_20200611_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='data',
            field=models.DateTimeField(null=True),
        ),
    ]
