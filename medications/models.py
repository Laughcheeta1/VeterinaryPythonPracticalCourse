from django.db import models
from appointments.models import Annotation_Appointment

# Create your models here.
class Medications(models.Model):
    name = models.CharField()
    manufacturer = models.CharField()
    description= models.CharField()

    def __str__(self):
        return self.name
    

class Medications_Sent(models.Model):
    annotation_appointment = models.ForeignKey(Annotation_Appointment, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medications, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instructions = models.CharField()

    def __str__(self):
        return str(self.medication) + " " + str(self.quantity)
