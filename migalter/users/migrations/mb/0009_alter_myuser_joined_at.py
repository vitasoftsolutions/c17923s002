# Generated by Django 4.2.3 on 2023-07-17 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_myuser_joined_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='joined_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 18, 3, 32, 34, 3292), null=True),
        ),
    ]
