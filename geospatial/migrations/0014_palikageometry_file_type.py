# Generated by Django 4.1 on 2024-04-08 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0013_palikageometry_bbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='palikageometry',
            name='file_type',
            field=models.CharField(blank=True, choices=[('shapefile', 'Shapefile'), ('geojson', 'GeoJSON')], default='shapefile', max_length=100, null=True),
        ),
    ]
