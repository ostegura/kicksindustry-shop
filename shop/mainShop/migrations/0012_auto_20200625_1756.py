# Generated by Django 3.0.5 on 2020-06-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0011_auto_20200625_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
