# Generated by Django 4.0.5 on 2023-10-21 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wearhouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialpurchase',
            name='purchase_code',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]