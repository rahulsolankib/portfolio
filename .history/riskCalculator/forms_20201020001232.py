from django import forms

from .models import Que,RiskModel


class QForm(forms.Form):
    ques1 = forms.CharField(widget = forms.RadioSelect,choices=DISPLAY_CHOICES)
    ques2 = forms.CharField()
    ques3 = forms.CharField()
    ques4 = forms.CharField()
    ques5 = forms.CharField()


class QueForm(forms.ModelForm):
    class Meta:
        model = Que
        fields = ['ques1','ques2','ques3','ques4','ques5']


class RiskForm(forms.ModelForm):
    class Meta:
        model = RiskModel
        fields = ['userid','risk_score']