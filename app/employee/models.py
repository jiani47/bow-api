from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)