from django.db import models
from pets.models import Pet
from veterinarians.models import Veterinarian

# Create your models here.
class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    motive = models.CharField(max_length=250)
    date = models.DateTimeField()
    diagnosis = models.CharField(max_length=1000)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.SET_NULL, null=True)

    def to_dict(self):
        return {
            "date": self.date,
            "motive": self.motive,
            "diagnosis": self.diagnosis,
            "pet": self.pet,
        }
    
    def __str__(self):
        return str(self.pet) + ", " + self.motive


class Annotation_Appointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    annotation = models.CharField()

    def __str__(self):
        return str(self.appointment) + self.annotation[0: 10]  # Get only the first 10 characters of the annotation

