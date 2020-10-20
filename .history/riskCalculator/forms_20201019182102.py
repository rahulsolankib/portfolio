from django import forms

from .models import Que

class QueForm(forms.ModelForm):
    class Meta:
        model = Que
        fields = ['ques2','ques2','ques3','ques4','ques5']