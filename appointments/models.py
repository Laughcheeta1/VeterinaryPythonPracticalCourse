from django.db import models
from pets.models import Pet

# Create your models here.
class Appointment(models.Model):
    date = models.DateField()
    motive = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=1000)
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL)
