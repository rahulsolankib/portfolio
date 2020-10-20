from django import forms

from .models import Que,RiskModel


class QForm(forms.Form):
    age_group=(
            ('1','Less than 25 years')
            ,('2','25-35 years')
            ,('3','36-40 years')
            ,('4','51 above')
    )

    ques1 = forms.TypedChoiceField(label='Which age group do you belong?',choices=age_group, coerce=int, initial=1)
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