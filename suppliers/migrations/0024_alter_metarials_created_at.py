# Generated by Django 4.2.3 on 2023-10-05 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0023_alter_metarials_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metarials',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 5, 19, 54, 0, 263226), null=True),
        ),
    ]
