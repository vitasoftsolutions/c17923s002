# Generated by Django 4.0.5 on 2023-10-21 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0023_alter_loaninstallment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaninstallment',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 10, 21), null=True),
        ),
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 10, 21), null=True),
        ),
    ]