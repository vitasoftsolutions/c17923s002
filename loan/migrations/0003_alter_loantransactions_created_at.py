# Generated by Django 4.2.3 on 2023-08-31 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_alter_loantransactions_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 8, 31), null=True),
        ),
    ]
