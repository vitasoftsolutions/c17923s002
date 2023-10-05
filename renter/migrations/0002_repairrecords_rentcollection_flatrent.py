# Generated by Django 4.2.3 on 2023-10-05 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0066_alter_common_created_at_alter_commonmodel_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0006_propertyinstallment_expensebyproperty'),
        ('renter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepairRecords',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.commonmodel')),
                ('reason', models.TextField()),
                ('amount', models.FloatField()),
                ('expensed_by', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Renter', 'Renter')], max_length=50, null=True)),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo')),
                ('property_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels')),
                ('renter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries')),
            ],
            bases=('globalapp2.commonmodel',),
        ),
        migrations.CreateModel(
            name='RentCollection',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.commonmodel')),
                ('rent_amount', models.FloatField()),
                ('due_amount', models.FloatField()),
                ('rent_date', models.DateField()),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo')),
                ('property_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels')),
                ('renter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries')),
            ],
            bases=('globalapp2.commonmodel',),
        ),
        migrations.CreateModel(
            name='FlatRent',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.commonmodel')),
                ('advanced_amount', models.FloatField()),
                ('due_amount', models.FloatField()),
                ('author_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projectinfo')),
                ('property_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.propertymodels')),
                ('renter_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='renter.renterbeneficaries')),
            ],
            bases=('globalapp2.commonmodel',),
        ),
    ]
