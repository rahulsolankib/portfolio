from django import forms

from .models import Questions

class Questionsform(forms.ModelForm):
    class Meta:
        model = Questions