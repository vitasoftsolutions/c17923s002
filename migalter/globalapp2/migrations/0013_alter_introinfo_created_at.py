# Generated by Django 4.2.3 on 2023-08-30 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0012_remove_introinfo_phone_number_phonenumber_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 30, 14, 39, 45, 938528), null=True),
        ),
    ]