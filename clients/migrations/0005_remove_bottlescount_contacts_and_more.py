# Generated by Django 4.1 on 2022-08-26 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_bottlescount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottlescount',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='bottlescount',
            name='name',
        ),
    ]
