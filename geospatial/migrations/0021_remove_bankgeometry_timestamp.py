# Generated by Django 4.1 on 2024-04-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0020_bankgeometry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankgeometry',
            name='timestamp',
        ),
    ]
