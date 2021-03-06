# Generated by Django 3.0.1 on 2020-04-13 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('email', models.EmailField(max_length=254)),
                ('question', models.TextField()),
                ('reply', models.TextField(default=None, null=True)),
                ('replied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('product', models.CharField(choices=[('0', 'Choose product..'), ('1', 'Sanitizer'), ('2', 'Antibiotics'), ('3', 'Amoxol-23'), ('4', 'Hydroxly-Peroxide'), ('5', 'Paracetamol'), ('6', 'Heat rub'), ('7', 'Amole'), ('8', 'JK4')], default='0', max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(choices=[('0', 'Select Your country..'), ('1', 'Zimbabwe'), ('2', 'Zambia'), ('3', 'South Africa'), ('4', 'Virgin Islands'), ('5', 'Algeria'), ('6', 'Botswana'), ('7', 'Cameroon'), ('8', 'Germany'), ('9', 'Other')], default='0', max_length=30)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]
