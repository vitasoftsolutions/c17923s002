# Generated by Django 4.0.5 on 2023-10-24 07:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_employee_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 24, 13, 34, 1, 376106), null=True),
        ),
    ]
