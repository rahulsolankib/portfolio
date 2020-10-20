from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Questions
from .forms import QuestionsForm,ActualQuestions
# Create your views here.
def ActualQuestions(request):
    # userid = User.objects.get(username=1).pk
    form = ActualQuestions(request.POST or None)

    # score = ((formRec['ques1'] + formRec['ques2'] + formRec['ques3'] + formRec['ques4'] + formRec['ques5'])/5.0) * 100.0 
    data = {'userid': 1,'risk_score':22}

    # formRec = QuestionsForm(data)
    # if formRec.is_valid() :
    #     formRec.save()
    context = {
        'form':form
    }
    return render(request,'riskCalculator//questions.html',form)