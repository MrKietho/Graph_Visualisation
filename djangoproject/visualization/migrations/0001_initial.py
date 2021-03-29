# Generated by Django 2.2.1 on 2019-06-13 16:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visualization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Data', models.FileField(upload_to='visual/', validators=[django.core.validators.FileExtensionValidator(['csv', 'json'])])),
            ],
        ),
    ]
