from django.db import models

# Create your models here.
class TecherModel(models.Model):
    username = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=30)


class Timetable(models.Model):
    name=models.CharField(max_length=30)
    date = models.DateField()
    time=models.TimeField()
    subject=models.CharField(max_length=50)