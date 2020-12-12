# Generated by Django 3.1.1 on 2020-12-12 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created', models.DateField(default='2020-12-12')),
                ('due_date', models.DateField(default='2020-12-12')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ToDoList.category')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
