from django import forms
from .models import Medications

class MedicationsForm(forms.ModelForm):
    class Meta:
        model = Medications
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'manufacturer': 'Fabricante',
            'description': 'Descripcion',
        }