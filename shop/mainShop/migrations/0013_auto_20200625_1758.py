# Generated by Django 3.0.5 on 2020-06-25 14:58

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0012_auto_20200625_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=('model', 'category__sex'), unique=True),
        ),
    ]
