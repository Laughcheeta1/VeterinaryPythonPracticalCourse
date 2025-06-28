from django.db import models

# Create your models here.
class Medications(models.Model):
    name = models.CharField()
    manufacturer = models.CharField()
    description= models.CharField()
