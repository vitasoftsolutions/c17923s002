# Generated by Django 4.0.5 on 2023-10-22 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerBeneficaries',
            fields=[
                ('beneficaries_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.beneficaries')),
            ],
            bases=('globalapp2.beneficaries',),
        ),
    ]
