from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Questions
from .forms import QuestionsForm,ActualQuestions
# Create your views here.
def questions(request):
    # userid = User.objects.get(username=1).pk
    formRec = ActualQuestions(request.POST or None)

    # score = ((formRec['ques1'] + formRec['ques2'] + formRec['ques3'] + formRec['ques4'] + formRec['ques5'])/5.0) * 100.0 
    data = {'userid': 1,'risk_score':22}

    formRec = QuestionsForm(data)
    if form.is_valid() :
        form.save()
    context = {
        'form':formRec
    }
    return render(request,'riskCalculator//questions.html',formRec)