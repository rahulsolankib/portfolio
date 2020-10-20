from django import forms

from .models import Que,RiskModel


class QForm(forms.Form):
    age_group=(
            (4,'Less than 25 years')
            ,(3,'25-35 years')
            ,(2,'36-40 years')
            ,(1,'51 above')
    )

    returnyear_group=(
            (1,'less than 2 years')
            ,(2,'2-5 years')
            ,(3,'more than 5 years')
    )

    experience_group=(
            (1,'Limited: I have very little investment experience outside of bank savings accounts andtime deposits. Slightly related')
            ,(2,'')
            ,(3,'Moderate: I have some experience investing')
    )

    ques1 = forms.TypedChoiceField(label='Which age group do you belong?',choices=age_group, coerce=int, initial=4)
    ques2 = forms.TypedChoiceField(label='When do you think you need your capital?',choices=returnyear_group, coerce=int, initial=1)
    ques3 = forms.TypedChoiceField(label='Your investment experience is best described as follows: ',choices=experience_group, coerce=int, initial=1)
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