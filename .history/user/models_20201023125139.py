from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.
class Personal_Info():
    email = forms.EmailField()
    name = forms.CharField(label='Your name')  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone = forms.CharField(label='Your Whatsapp number',validators=[phone_regex])