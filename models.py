from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=15)
    email = models.EmailField(unique=True)




# Create your models here.
