# Generated by Django 4.2.3 on 2023-09-10 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_loanbeneficaries_appointment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanbeneficaries',
            name='appointment',
        ),
    ]
