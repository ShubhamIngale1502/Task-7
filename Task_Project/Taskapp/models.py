from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length = 45)
    email = models.EmailField()
    salary = models.IntegerField()
    address = models.TextField(null=True, blank=True)

