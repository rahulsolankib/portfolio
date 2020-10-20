from django.db import models
from django import forms

# Create your models here.
class userModel(models.Model):
    email = forms.EmailField()
    name = forms.CharField(label='Your name')  