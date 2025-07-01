from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date
import common.validator as custom_validations
from datetime import date

# Create your models here.
class User(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(1)]
        )
    phone_number = models.CharField(
        max_length=14, 
        validators=[MinLengthValidator(10), custom_validations.verify_number]
        )
    address = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(1)]
        )
    birth_day = models.DateField(
        validators=[],
    )
    
    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_day.year - ((today.month, today.day) < (self.birth_day.month, self.birth_day.day))
    
    def __str__(self):
        return self.name
    
    def to_dict(self):
        return { 
            'Nombre': self.name, 
            'Numero de celular': self.phone_number, 
            'Direccion': self.address,
            'Edad': self.age,
            'Fecha de nacimiento': self.birth_day,
        }
