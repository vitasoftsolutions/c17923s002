# Generated by Django 4.0.5 on 2023-12-06 10:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaninstallment',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 6), null=True),
        ),
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 6), null=True),
        ),
    ]
