# Generated by Django 4.2.3 on 2023-09-18 19:18

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
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 19, 1, 18, 41, 272435), null=True),
        ),
    ]