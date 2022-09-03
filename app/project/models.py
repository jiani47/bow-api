
from django.contrib.auth.models import User
from employee import models as employee_models
from django.db import models 
# Create your models here.

class Project(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    priority = models.SmallIntegerField()
    owner = models.ForeignKey(employee_models.Employee, on_delete=models.deletion.CASCADE)
    status = models.CharField(max_length=255)
    target_delivery_date = models.DateField()
    estimated_delivery_date = models.DateField()
    actual_delivery_date = models.DateField()

    def __str__(self):
        return self.name # this affects how it will be displayed in django admin
