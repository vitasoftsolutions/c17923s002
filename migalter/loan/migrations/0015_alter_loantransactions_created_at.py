# Generated by Django 4.2.3 on 2023-08-31 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0014_alter_loantransactions_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 4, 13, 50, 290518, tzinfo=datetime.timezone.utc)),
        ),
    ]