from django.db import models

# Create your models here.
class Appointment(models.Model):
    date = models.DateField()
    motive = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=1000)
    # Todo add the pet

