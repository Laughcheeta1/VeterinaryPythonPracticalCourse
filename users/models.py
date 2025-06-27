from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(1)]
        )
    phone_number = models.CharField(
        max_length=14, 
        validators=[MinLengthValidator(10)]
        )
    address = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(1)]
        )
    
    def __str__(self):
        return self.name + ", " + self.phone_number
