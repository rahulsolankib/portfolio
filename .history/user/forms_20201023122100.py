from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Your name')  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    
    phone = forms.CharField(label='Your Whatsapp number',validators=[phone_regex])
    class Meta:
        model = User
        model.name = 'name'
        model.phone = '1233333555565'
        fields = ['username','email','name','phone','password1','password2']