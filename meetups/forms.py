from dataclasses import field
from django import forms
from .models import Paticipants

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Paticipants
        fields = '__all__'
