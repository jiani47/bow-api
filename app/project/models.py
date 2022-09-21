
from django.contrib.auth.models import User
from employee import models as employee_models
from django.db import models 
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, default="")
    priority = models.SmallIntegerField()
    status = models.CharField(max_length=255)
    target_delivery_date = models.DateField(null=True)
    estimated_delivery_date = models.DateField(null=True)
    actual_delivery_date = models.DateField(null=True)

    def __str__(self):
        return self.name # this affects how it will be displayed in django admin
