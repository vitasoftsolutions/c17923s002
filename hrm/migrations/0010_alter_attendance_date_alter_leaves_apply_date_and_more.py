# Generated by Django 4.2.3 on 2023-09-13 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0009_alter_attendance_date_alter_leaves_apply_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 13, 13, 24, 33, 282408), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='apply_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 13, 13, 24, 33, 282408), null=True),
        ),
        migrations.AlterField(
            model_name='salaries',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 13, 13, 24, 33, 282408), null=True),
        ),
    ]
