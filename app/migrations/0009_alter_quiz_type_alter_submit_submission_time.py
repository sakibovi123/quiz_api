# Generated by Django 4.0.6 on 2022-07-07 03:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_quiz_quiz_type_quiz_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 6, 20, 23, 33, 656414)),
        ),
    ]