# Generated by Django 4.1 on 2024-04-08 05:40

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0007_palikageometry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palikageometry',
            name='district',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, max_length=100, null=True, srid=4326),
        ),
    ]
