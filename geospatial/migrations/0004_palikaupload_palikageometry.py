# Generated by Django 4.1 on 2024-04-05 11:26

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geospatial', '0003_alter_geospatialdata_data_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalikaUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file', models.FileField(blank=True, null=True, upload_to='geospatialdata/')),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PalikaGeometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('palika_name', models.CharField(blank=True, max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('file_type', models.CharField(blank=True, max_length=100, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
