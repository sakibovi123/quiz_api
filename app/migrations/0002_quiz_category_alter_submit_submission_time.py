# Generated by Django 4.0.6 on 2022-07-06 05:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 5, 22, 30, 32, 639170)),
        ),
    ]
