# Generated by Django 4.2.3 on 2023-08-31 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0005_alter_introinfo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 11, 50, 25, 446638), null=True),
        ),
    ]