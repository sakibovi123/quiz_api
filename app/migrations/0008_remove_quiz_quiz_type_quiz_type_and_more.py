# Generated by Django 4.0.6 on 2022-07-07 03:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_quiztype_type_alter_submit_submission_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='quiz_type',
        ),
        migrations.AddField(
            model_name='quiz',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.type'),
        ),
        migrations.AlterField(
            model_name='submit',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 6, 20, 22, 14, 503697)),
        ),
    ]
