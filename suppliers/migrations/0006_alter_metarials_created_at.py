# Generated by Django 4.2.3 on 2023-10-03 08:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_alter_metarials_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metarials',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 3, 14, 6, 25, 228753), null=True),
        ),
    ]