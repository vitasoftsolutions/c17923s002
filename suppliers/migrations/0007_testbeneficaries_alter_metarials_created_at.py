# Generated by Django 4.2.3 on 2023-10-03 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globalapp2', '0046_alter_common_created_at_alter_introinfo_created_at_and_more'),
        ('suppliers', '0006_alter_metarials_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestBeneficaries',
            fields=[
                ('beneficaries_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.beneficaries')),
            ],
            bases=('globalapp2.beneficaries',),
        ),
        migrations.AlterField(
            model_name='metarials',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 3, 14, 20, 28, 475748), null=True),
        ),
    ]
