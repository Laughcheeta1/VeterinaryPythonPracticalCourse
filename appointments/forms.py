from django import forms
from .models import Appointment
from datetime import datetime, timedelta

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'min': self._get_date_appointment(),
        })

    def _get_date_appointment(self):
        """Return the minimum date for the select datetime in the html form"""
        pass  # TODO
    
    def _get_next_30_min_interval(self):
        """Round datetime up to the nearest 30-minute interval"""
        now = datetime.now()
        
        # Calculate minutes to add to reach next 30-minute mark
        current_minutes = now.minute
        if current_minutes < 30:
            target_minutes = 30
        else:
            target_minutes = 0
            now += timedelta(hours=1)  # Next hour
        
        rounded_time = now.replace(minute=target_minutes, second=0, microsecond=0)
        return rounded_time.strftime('%Y-%m-%dT%H:%M')
    
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'motive': forms.TextInput(),
            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control date-picker',
                'max': f'{datetime.now().year}-12-31T18:00',
                'step': '1800',
                }),
            'diagnosis': forms.Textarea(),
        }
        help_texts = {
            'phone_number': 'Puedes ingresar tu numero de celular con o sin el codigo del pais'
        }