# Generated by Django 5.0.3 on 2024-03-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_options_rename_complete_task_is_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('WK', 'Work'), ('PRSNL', 'Personal'), ('STDY', 'Study'), ('HLT', 'Health'), ('FNS', 'Finance'), ('HM', 'Home'), ('SCL', 'Social'), ('SPNG', 'Shopping'), ('ENTNT', 'Entertainment')], default='WK', max_length=5),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_hours',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]