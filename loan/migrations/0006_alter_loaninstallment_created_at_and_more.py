# Generated by Django 4.2.3 on 2023-12-31 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_alter_loaninstallment_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loaninstallment',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 31), null=True),
        ),
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 12, 31), null=True),
        ),
    ]
