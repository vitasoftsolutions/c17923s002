# Generated by Django 4.0.5 on 2023-10-27 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0008_alter_attendance_date_alter_leaves_apply_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 27, 17, 13, 45, 499907), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='apply_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 27, 17, 13, 45, 499907), null=True),
        ),
        migrations.AlterField(
            model_name='salaries',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 27, 17, 13, 45, 503123), null=True),
        ),
    ]
