from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    semester = models.IntegerField()