from re import T
from django.db import models
from sqlite3 import IntegrityError
from datetime import datetime, date

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=200, unique=True,verbose_name='Name')
    age = models.CharField(max_length=200, verbose_name='Age')
    gender= models.CharField(max_length=10, verbose_name="Gender", null=True)
    department= models.CharField(max_length=100, verbose_name="Department", null=True)
    dob= models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)


    def __str__(self) -> str:
        return self.name

