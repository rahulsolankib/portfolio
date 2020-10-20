from django import forms

from .models import Que,RiskModel


class QForm(forms.Form):
    subject_code=(

            (1,'CS101')
            ,(2,'CS102')
            ,(3,'CS103')
            ,(4,'CS104')
            ,(5,'CS105')
            ,(6,'CS106')
    )

    ques1 = forms.CharField(choices=subject_code)
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