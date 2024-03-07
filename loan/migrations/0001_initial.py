# Generated by Django 4.0.5 on 2023-10-22 14:08

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globalapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanBeneficaries',
            fields=[
                ('beneficaries_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='globalapp2.beneficaries')),
            ],
            bases=('globalapp2.beneficaries',),
        ),
        migrations.CreateModel(
            name='LoanInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('instalment', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('document', models.FileField(upload_to='documents')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(blank=True, default=datetime.date(2023, 10, 22), null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(1)])),
                ('return_type', models.CharField(blank=True, choices=[('Fixed', 'Fixed'), ('Percentage', 'Percentage')], max_length=50, null=True)),
                ('interest', models.FloatField()),
                ('instalment', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('interested_amount', models.FloatField(blank=True, null=True)),
                ('return_amount', models.FloatField(blank=True, null=True)),
                ('current_amount', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('last_payed', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(blank=True, default=datetime.date(2023, 10, 22), null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('giver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_loans', to='loan.loanbeneficaries')),
                ('taker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_loans', to='loan.loanbeneficaries')),
            ],
        ),
    ]
