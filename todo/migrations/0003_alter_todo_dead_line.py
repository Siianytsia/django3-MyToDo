# Generated by Django 4.0.6 on 2022-08-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_todolist_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dead_line',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
