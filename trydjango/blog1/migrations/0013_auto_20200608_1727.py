# Generated by Django 2.2.2 on 2020-06-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0012_auto_20200608_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(null=True),
        ),
    ]
