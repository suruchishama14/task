# Generated by Django 3.0.8 on 2021-04-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210403_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
    ]
