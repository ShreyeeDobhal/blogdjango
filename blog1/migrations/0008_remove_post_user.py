# Generated by Django 2.2.2 on 2020-06-06 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0007_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
