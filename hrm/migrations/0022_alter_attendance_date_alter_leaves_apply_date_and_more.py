# Generated by Django 4.2.3 on 2023-09-18 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0021_alter_attendance_date_alter_leaves_apply_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 18, 12, 25, 36, 644355), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='apply_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 18, 12, 25, 36, 645013), null=True),
        ),
        migrations.AlterField(
            model_name='salaries',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 18, 12, 25, 36, 645461), null=True),
        ),
    ]
