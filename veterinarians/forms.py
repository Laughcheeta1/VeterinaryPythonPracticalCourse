from django import forms
from .models import Veterinarian

class VeterinarianForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = '__all__'