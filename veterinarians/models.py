from django.db import models
from django.core.validators import MinLengthValidator
import common.validator as custom_validations

# Create your models here.
class Veterinarian_Specialties(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Veterinarian(models.Model):
    name = models.CharField()
    phone_number = models.CharField(
        max_length=14, 
        validators=[MinLengthValidator(10), custom_validations.verify_number]
        )
    license_number = models.CharField()
    specialty = models.ForeignKey(Veterinarian_Specialties, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    def basic_info(self):
        return {
            'name': self.name,
            'specialty': self.specialty,
        }

    def complete_info(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'license_number': self.license_number,
            'specialty': self.specialty,
        }
    