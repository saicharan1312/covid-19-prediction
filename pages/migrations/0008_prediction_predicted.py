# Generated by Django 3.0.7 on 2020-07-24 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_remove_prediction_td'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='predicted',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
