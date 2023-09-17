# Generated by Django 4.2.3 on 2023-08-31 04:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntroInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('present_address', models.TextField()),
                ('permanent_address', models.TextField(null=True)),
                ('NID_number', models.CharField(max_length=20)),
                ('nid_front', models.FileField(blank=True, null=True, upload_to='nid/', verbose_name='NID Image (Front)')),
                ('nid_back', models.FileField(blank=True, null=True, upload_to='nid/', verbose_name='NID Image (Back)')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('appointment', models.FileField(blank=True, null=True, upload_to='appointment/')),
                ('status', models.BooleanField(blank=True, default=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 31, 10, 51, 11, 921259), null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('relation', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Beneficaries',
            fields=[
                ('introinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.introinfo')),
            ],
            bases=('globalapp2.introinfo',),
        ),
    ]
