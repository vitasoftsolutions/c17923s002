# Generated by Django 4.0.5 on 2024-03-06 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_alter_assetssell_documents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetssell',
            old_name='documents',
            new_name='file',
        ),
    ]