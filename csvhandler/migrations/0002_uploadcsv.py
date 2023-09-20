# Generated by Django 4.2.3 on 2023-09-20 08:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvhandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='csv', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])])),
            ],
        ),
    ]
