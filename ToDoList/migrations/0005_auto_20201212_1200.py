# Generated by Django 3.1.1 on 2020-12-12 19:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0004_auto_20201212_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 19, 0, 16, 608744, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 12, 19, 0, 16, 608744, tzinfo=utc)),
        ),
    ]
