# Generated by Django 4.1 on 2024-04-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0010_palikageometry_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='palikageometry',
            name='area',
            field=models.FloatField(blank=True, null=True),
        ),
    ]