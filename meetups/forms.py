from django import forms
from .models import Paticipants
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Paticipants
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    fullname = forms.CharField(label='Full Name')
    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(CreateUserForm, self).save(commit=False)
            user.fullname = self.cleaned_data["fullname"]
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
