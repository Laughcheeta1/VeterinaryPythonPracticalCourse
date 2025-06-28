from django.db import models
from pets.models import Pet

# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField()
    motive = models.CharField(max_length=250)
    diagnosis = models.CharField(max_length=1000)
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)

    def to_dict(self):
        return {
            "date": self.date,
            "motive": self.motive,
            "diagnosis": self.diagnosis,
            "pet": self.pet,
        }
    
    def __str__(self):
        return str(self.pet) + ", " + self.motive
