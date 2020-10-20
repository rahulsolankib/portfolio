from django import forms

from .models import Que

class QueForm(forms.ModelForm):
    class Meta:
        model = Que