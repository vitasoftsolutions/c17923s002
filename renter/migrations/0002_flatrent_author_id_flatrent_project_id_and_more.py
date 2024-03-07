# Generated by Django 4.0.5 on 2023-12-06 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_expensebyproperty_author_id_and_more'),
        ('renter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatrent',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flatrent',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo'),
        ),
        migrations.AddField(
            model_name='flatrent',
            name='property_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels'),
        ),
        migrations.AddField(
            model_name='flatrent',
            name='renter_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries'),
        ),
        migrations.AddField(
            model_name='rentcollection',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rentcollection',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo'),
        ),
        migrations.AddField(
            model_name='rentcollection',
            name='property_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels'),
        ),
        migrations.AddField(
            model_name='rentcollection',
            name='renter_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries'),
        ),
        migrations.AddField(
            model_name='repairrecords',
            name='author_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='repairrecords',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo'),
        ),
        migrations.AddField(
            model_name='repairrecords',
            name='property_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels'),
        ),
        migrations.AddField(
            model_name='repairrecords',
            name='renter_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries'),
        ),
    ]
