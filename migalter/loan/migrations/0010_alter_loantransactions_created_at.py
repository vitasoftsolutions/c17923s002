# Generated by Django 4.2.3 on 2023-08-30 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0009_alter_loantransactions_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 30, 8, 44, 35, 885712, tzinfo=datetime.timezone.utc)),
        ),
    ]
