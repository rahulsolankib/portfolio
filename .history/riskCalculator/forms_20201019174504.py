from django import forms

from .models import Questions

class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'userid','risk_score'
        ]

class ActualQuestions(forms.ModelForm):
    class Meta:
        model = Actual