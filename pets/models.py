from django.db import models
from users.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Pet(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    birthday = models.DateField()
    species = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    race = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)]
        )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL)
