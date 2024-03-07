# Generated by Django 4.2.3 on 2023-08-30 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0011_alter_introinfo_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introinfo',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='relation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 30, 14, 26, 6, 493140), null=True),
        ),
    ]
