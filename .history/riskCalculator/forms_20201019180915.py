from django import forms

from .models import Actual

# class QuestionsForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         fields = [
#             'userid','risk_score'
#         ]

class ActualQuestions(forms.ModelForm):
    class Meta:
        model = Actual
        fields = [
            'ques1','ques2','ques3','ques4','ques5'
        ]   