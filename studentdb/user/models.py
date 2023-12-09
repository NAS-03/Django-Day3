from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,
                             null = False,
                             unique= True)
    mobile_no = models.CharField(max_length=10)
    grade = models.IntegerField()
    faculty = models.CharField(max_length=50)