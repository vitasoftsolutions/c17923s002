# Generated by Django 4.2.3 on 2023-08-15 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_alter_loantransactions_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 15, 5, 42, 37, 574194, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='loantransactions',
            name='interested_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
