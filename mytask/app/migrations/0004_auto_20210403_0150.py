# Generated by Django 3.0.8 on 2021-04-02 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_timetable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='day',
            new_name='date',
        ),
    ]
