# Generated by Django 4.2.3 on 2023-09-10 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0004_alter_loantransactions_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanbeneficaries',
            name='appointment',
            field=models.FileField(blank=True, null=True, upload_to='appointment/'),
        ),
        migrations.AlterField(
            model_name='loantransactions',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.date(2023, 9, 10), null=True),
        ),
    ]