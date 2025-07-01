from django import forms
from .models import User
import re

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

    def clean_phone_number(self):
        # Take into account that to get here, the number must have passed the validator for the phone number
        phone = self.cleaned_data.get('phone_number')
        if not phone:
            return phone
        
        phone = re.sub(' ', '', phone)

        # Case one: does not have a country identifier
        if len(phone) == 10:
            # Assume the phone is from Colombia
            return f'+57 {phone[:3]} {phone[3:6]} {phone[6:]}'
        
        # Case two: they added the country code with the '+'
        elif phone[0] == '+':
            # This is because all the country codes are not the same. Ex: US = +1, COL = +57
            number_start = len(phone) - 10
            return f'{phone[:number_start]} {phone[number_start:number_start + 3]} {phone[number_start + 3:number_start + 6]} {phone[number_start + 6:]}'

        # Case three: country code without the '+'
        else:
            number_start = len(phone) - 10
            return f'+{phone[:number_start]} {phone[number_start:number_start + 3]} {phone[number_start + 3:number_start + 6]} {phone[number_start + 6:]}'
        