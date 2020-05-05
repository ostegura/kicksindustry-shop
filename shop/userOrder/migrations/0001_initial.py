# Generated by Django 3.0.5 on 2020-05-01 19:36

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=64)),
                ('surname', models.CharField(default='Surname', max_length=64)),
                ('address', models.CharField(default='Address', max_length=128)),
                ('phone_no', models.CharField(default='1234567890', max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\d+)*\\Z'), code='invalid', message=None), django.core.validators.MinLengthValidator(10)], verbose_name='Phone number')),
                ('email', models.EmailField(default='defaultemail@django.com', max_length=128)),
                ('shoes_name', models.CharField(default='Shoes name', max_length=64)),
                ('model', models.CharField(max_length=128)),
                ('size', models.CharField(default='', max_length=2)),
                ('time', models.DateTimeField(auto_now=True, verbose_name='order time')),
                ('mod_check', models.BooleanField(default=False)),
            ],
        ),
    ]