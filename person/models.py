from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=20)
    salary = models.FloatField(null=True, blank=True)
    department = models.CharField(max_length=20)


class Department(models.Model):
    name = models.CharField(max_length=20)