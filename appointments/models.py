from django.db import models
from pets.models import Pet
from veterinarians.models import Veterinarian

# Create your models here.
class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    motive = models.CharField(max_length=250)
    date = models.DateTimeField()
    diagnosis = models.CharField(null=True)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.SET_NULL, null=True)        
    
    def basic_info(self):
        return {
            "Fecha": self.date,
            "Mascota": self.pet,
        }

    def complete_info(self):
        return {
            "Fecha": self.date,
            "Motivo": self.motive,
            "Diagnosis": self.diagnosis,
            "Mascota": self.pet,
            "Veterinario": self.veterinarian
        }
    
    def __str__(self):
        return str(self.pet) + ", " + self.motive


class Annotation_Appointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    annotation = models.CharField()

    def __str__(self):
        return str(self.appointment) + self.annotation[0: 10]  # Get only the first 10 characters of the annotation

