from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Jhon Doe'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': '+57 311 123 4567'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Cra. 48 #18A 14 piso 5, Medellin'
            }),
            'birth_day': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control date-picker',
            }),
        }
        help_texts = {
            'phone_number': 'Puedes ingresar tu numero de celular con o sin el codigo del pais'
        }
        labels = {
            'name': 'Nombre',
            'phone_number': 'Numero de telefono',
            'address': 'Direccion',
            'birth_day': 'Fecha de nacimiento'
        }