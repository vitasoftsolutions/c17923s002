# Generated by Django 4.2.3 on 2023-08-30 12:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_employee_joined_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joined_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 30, 18, 12, 25, 42749), null=True),
        ),
    ]
