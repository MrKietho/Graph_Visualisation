# Generated by Django 2.0.7 on 2019-06-14 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visualization',
            name='Date',
            field=models.DateField(default=datetime.datetime(2019, 6, 14, 11, 51, 6, 776067)),
        ),
    ]