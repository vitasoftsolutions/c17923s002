# Generated by Django 4.0.5 on 2023-12-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_expensebyproperty_author_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectinfo',
            name='image',
            field=models.ImageField(default=None, upload_to='upload'),
        ),
    ]
