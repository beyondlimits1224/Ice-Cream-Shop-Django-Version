from django.db import models

# Create your models here.

# Create a table
class Icecreamshop(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)