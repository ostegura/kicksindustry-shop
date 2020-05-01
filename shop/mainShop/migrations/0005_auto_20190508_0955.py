# Generated by Django 2.1.3 on 2019-05-08 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainShop', '0004_auto_20190507_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='sale_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 6, 55, 55, 297930, tzinfo=utc), verbose_name='added date'),
        ),
    ]