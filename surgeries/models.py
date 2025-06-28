from django.db import models
from pets.models import Pet

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
    date = models.DateTimeField()
    surgeon = models.CharField()
    type = models.ForeignKey(Surgery_Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.surgeon + " on " + str(self.pet)
    
    def to_dict(self):
        return {
            'pet': self.pet,
            'date': self.date,
            'surgeon': self.surgeon,
            'type': self.type
        }
