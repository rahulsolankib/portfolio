from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Create your models here.
class Personal_Info(models.Model):
    username = models.CharField(max_length = 120)
    email = models.CharField(max_length = 120)
    name = models.CharField(max_length = 120)  
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone = models.CharField(validators=[phone_regex])