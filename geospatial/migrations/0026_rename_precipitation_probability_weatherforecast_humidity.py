# Generated by Django 4.1 on 2024-04-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0025_alter_weatherforecast_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherforecast',
            old_name='precipitation_probability',
            new_name='humidity',
        ),
    ]