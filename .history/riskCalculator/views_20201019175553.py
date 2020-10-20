from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Questions
from .forms import QuestionsForm,ActualQuestions
# Create your views here.
def questions(request):
    userid = User.objects.get(username=User.username).pk
    formRec = ActualQuestions(request.POST or None)

    score = ((formRec['ques1'] + formRec['ques2'] + formRec['ques3'] + formRec['ques4'] + formRec['ques5'])/5.0) * 100.0 
    data = {'userid': userid,'risk_score':score}

    form = QuestionsForm(data)
    if form.is_valid() :
        form.save()
    context = {
        'form':form
    }
    return render(request,'riskCalculator//questions.html',context)