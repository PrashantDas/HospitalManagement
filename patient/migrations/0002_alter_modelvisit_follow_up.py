# Generated by Django 4.1 on 2023-07-27 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelvisit',
            name='follow_up',
            field=models.DateField(default=datetime.datetime(2023, 8, 26, 5, 43, 50, 936908)),
        ),
    ]
