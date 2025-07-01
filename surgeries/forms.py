from django import forms
from .models import Surgery
from datetime import datetime

class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = '__all__'
        widgets = {
            # We are going to suppose the surgeries can be perfored at all hours
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control date-picker',
                'min': datetime.now().strftime('%Y-%m-%dT%H:%M'),
                'max': f'{datetime.now().year}-12-31T11:59',
                'step': '3600',
                }),
        }
        labels = {
            'pet': 'Mascota',
            'type': 'Typo de cirugia',
            'date': 'Fecha y hora',
            'surgeon': 'Cirujano',
        }