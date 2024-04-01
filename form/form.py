from .models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'email','password']
        
