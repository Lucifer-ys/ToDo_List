# Generated by Django 3.2 on 2021-04-15 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='tasks',
            table='todo',
        ),
    ]
