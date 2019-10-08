from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.TextField()
    major = models.TextField()