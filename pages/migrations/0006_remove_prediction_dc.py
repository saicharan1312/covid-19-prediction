# Generated by Django 3.0.7 on 2020-07-24 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_prediction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='dc',
        ),
    ]
