from django.db import models
from pets.models import Pet

# Create your models here.
class Surgery(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    surgeon = models.CharField()
