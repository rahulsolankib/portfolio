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
            ,(2,'Moderate: I have some experience investing')
            ,(3,'Extensive: I am an active and experienced investor')
    )

    income_status = (
        (1,'I expect my income to decrease')
        ,(2,'I expect my income to remain steady')
        ,(3,'I expect my income to increase')
    )

    percentage_invest = (
        (4,'Less than 25%')
        ,(3,'25 % - 50 %')
        ,(2,'50 % - 75 %')
        ,(1,'more than 75 %')
    )
    ques1 = forms.TypedChoiceField(label='Which age group do you belong?',choices=age_group, coerce=int, initial=4)
    ques2 = forms.TypedChoiceField(label='When do you think you need your capital?',choices=returnyear_group, coerce=int, initial=1)
    ques3 = forms.TypedChoiceField(label='Your investment experience is best described as follows: ',choices=experience_group, coerce=int, initial=1)
    ques4 = forms.TypedChoiceField(label='How will you describe your expected future income over the next 5 years? ',choices=income_status, coerce=int, initial=3)
    ques5 = forms.TypedChoiceField(label='How will you describe your expected future income over the next 5 years? ',choices=income_status, coerce=int, initial=3)
    ques6 = forms.TypedChoiceField(label='What is the percentage of your total wealth that you would like to invest? ',choices=percentage_invest, coerce=int, initial=3)


class QueForm(forms.ModelForm):
    class Meta:
        model = Que
        fields = ['ques1','ques2','ques3','ques4','ques5']


class RiskForm(forms.ModelForm):
    class Meta:
        model = RiskModel
        fields = ['userid','risk_score']