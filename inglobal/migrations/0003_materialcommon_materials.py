# Generated by Django 4.0.5 on 2023-10-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_alter_metarials_created_at'),
        ('inglobal', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialcommon',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, to='suppliers.metarials'),
        ),
    ]
