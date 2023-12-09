from django.db import models

# Create your models here.


class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    course_length = models.CharField(max_length=100)