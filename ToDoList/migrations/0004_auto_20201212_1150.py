# Generated by Django 3.1.1 on 2020-12-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0003_auto_20201211_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
