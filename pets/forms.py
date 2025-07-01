from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Noa'
            }),
            'species': forms.TextInput(attrs={
                'placeholder': 'Canino'
            }),
            'birthday': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control date-picker',
            }),
            'race': forms.TextInput(attrs={
                'placeholder': 'Fresh Puddle'
            }),
        }
        labels = {
            'name': 'Nombre',
            'birthday': 'Fecha de nacimiento',
            'species': 'Especie',
            'race': 'Raza',
            'owner': 'Dueno',
        }
