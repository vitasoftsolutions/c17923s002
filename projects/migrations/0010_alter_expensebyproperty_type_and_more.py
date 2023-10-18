# Generated by Django 4.2.3 on 2023-10-12 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0072_applabels_typess_remove_types_app_label_and_more'),
        ('projects', '0009_unitmodels_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensebyproperty',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globalapp2.typess'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='project_size_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_size_type', to='globalapp2.typess'),
        ),
        migrations.AlterField(
            model_name='projectinfo',
            name='project_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_type', to='globalapp2.typess'),
        ),
        migrations.AlterField(
            model_name='propertymodels',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globalapp2.typess'),
        ),
        migrations.AlterField(
            model_name='propertypurchase',
            name='payment_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globalapp2.typess'),
        ),
    ]