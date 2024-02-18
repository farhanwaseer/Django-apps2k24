from django.db import models

# Create your models here.

class Person(models.Model):
      Person_name = models.CharField(max_length=20)
      email = models.EmailField()
      phone = models.CharField(max_length=11)
      age = models.CharField(max_length=10)