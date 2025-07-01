from django import forms
from .models import Appointment
from datetime import datetime, timedelta

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({
            'min': self._get_date_appointment(),
        })

    """
    Return the minimum date for the select datetime in the html form.

    That is, if the appointment is being registered before work hours, then make the minimum hour at the work ours.
    If the appointment is being registered after work hours, then make the minimum hour at work hours next day
    """
    def _get_date_appointment(self):
        now = datetime.now()
        start_hour = datetime(now.year, now.month, now.day, 9, 0, 0)
        
        if now < start_hour:
            return start_hour.strftime('%Y-%m-%dT%H:%M')
        
        last_turn = datetime(now.year, now.month, now.day, 17, 30, 0)
        return self._get_next_30_min_interval() if now < last_turn else (start_hour + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M')
    
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