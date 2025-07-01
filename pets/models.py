from django.db import models
from users.models import User
from django.core.validators import MinLengthValidator
from datetime import date

# Create your models here.
class Pet(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    birthday = models.DateField(
        validators=[]
    )
    species = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    race = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))        

    def to_dict(self):
        return {
            'Nombre': self.name,
            'Fecha de nacimiento': self.birthday,
            'Especie': self.species,
            'Raza': self.race,
            'Dueño': self.owner,
        }
    
    def __str__(self):
        return self.name
