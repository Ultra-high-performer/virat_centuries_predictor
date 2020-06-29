from django.db import models

# Create your models here.
class class_1(models.Model):
    name = models.CharField(max_length = 200 , null = True)
    year = models.CharField(max_length = 4   , null = True)
