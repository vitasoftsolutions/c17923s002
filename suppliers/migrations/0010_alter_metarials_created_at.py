# Generated by Django 4.2.3 on 2023-10-03 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0009_alter_metarials_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metarials',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 3, 18, 47, 16, 235994), null=True),
        ),
    ]