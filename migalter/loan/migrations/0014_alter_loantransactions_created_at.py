# Generated by Django 4.2.3 on 2023-08-31 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0013_remove_loanbeneficaries_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 3, 59, 55, 526912, tzinfo=datetime.timezone.utc)),
        ),
    ]
