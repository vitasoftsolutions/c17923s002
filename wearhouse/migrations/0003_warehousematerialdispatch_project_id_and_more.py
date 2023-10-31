# Generated by Django 4.0.5 on 2023-10-24 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
        ('wearhouse', '0002_wearhouseitem_quantity_warehousematerialdispatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehousematerialdispatch',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo'),
        ),
        migrations.AlterField(
            model_name='warehousematerialdispatch',
            name='warehouse_item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wearhouse.wearhouseitem'),
        ),
    ]
