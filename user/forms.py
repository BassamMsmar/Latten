from django import forms
from django.contrib.auth.models import  User


# Create your models here.
class FormRegisterUser(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
       
        model = User
        fields = (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name'
        )