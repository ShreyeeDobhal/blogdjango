# Generated by Django 2.2.2 on 2020-06-06 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0005_auto_20200606_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]
