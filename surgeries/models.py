from django.db import models
from pets.models import Pet
from veterinarians.models import Veterinarian
from common.validator import validate_surgeon
from appointments.models import Annotation_Appointment

class Surgery_Type(models.Model):
    name = models.CharField()

    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        return {
            'name' : self.name
        }


class Surgery(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Surgery_Type, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    surgeon = models.ForeignKey(
        Veterinarian, 
        on_delete=models.SET_NULL,
        null=True,
        # validators=[validate_surgeon],
        )

    def __str__(self):
        return str(self.surgeon) + " on " + str(self.pet)
    
    def basic_info(self):
        return {
            'pet': self.pet,
            'type': self.type
        }

    def complete_info(self):
        return {
            'pet': self.pet,
            'date': self.date,
            'surgeon': self.surgeon,
            'type': self.type
        }
    

class Surgeries_Sent(models.Model):
    annotation_appointment = models.ForeignKey(Annotation_Appointment, on_delete=models.CASCADE)
    surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.surgery)
