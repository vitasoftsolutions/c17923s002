# Generated by Django 4.2.3 on 2023-08-31 11:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0007_alter_introinfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumber',
            name='ben_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benid', to='globalapp2.beneficaries'),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='globalapp2.beneficaries'),
        ),
        migrations.AlterField(
            model_name='introinfo',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 17, 14, 50, 650099), null=True),
        ),
    ]