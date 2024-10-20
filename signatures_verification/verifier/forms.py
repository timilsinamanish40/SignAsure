from django import forms
from django.contrib.auth.models import User
from .models import Signature

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SignatureUploadForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['signature_image']
