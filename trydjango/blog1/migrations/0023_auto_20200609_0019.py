# Generated by Django 2.2.2 on 2020-06-09 12:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0022_auto_20200609_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 12, 19, 25, 602057, tzinfo=utc)),
        ),
    ]
