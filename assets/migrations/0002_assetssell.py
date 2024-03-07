# Generated by Django 4.0.5 on 2024-03-06 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0019_alter_common_created_at_alter_commonmodel_created_at_and_more'),
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetsSell',
            fields=[
                ('commonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.commonmodel')),
                ('name', models.CharField(max_length=100)),
                ('buyer_name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('buyer_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
            ],
            bases=('globalapp2.commonmodel',),
        ),
    ]