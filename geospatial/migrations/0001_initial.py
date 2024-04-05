# Generated by Django 4.1 on 2024-04-04 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoSpatialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('file_type', models.CharField(blank=True, max_length=100, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('data_file', models.FileField(upload_to='geospatialdata/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
