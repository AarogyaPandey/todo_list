# Generated by Django 4.1 on 2024-04-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geospatial', '0009_alter_palikageometry_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='palikageometry',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
