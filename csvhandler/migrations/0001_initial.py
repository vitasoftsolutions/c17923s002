# Generated by Django 4.0.5 on 2023-10-22 14:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('app_label', models.CharField(blank=True, max_length=50, null=True)),
                ('file', models.FileField(upload_to='csv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
            ],
        ),
    ]
