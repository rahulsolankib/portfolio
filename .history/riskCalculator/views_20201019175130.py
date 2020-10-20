from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Questions
from .forms import QuestionsForm,ActualQuestions
# Create your views here.
def questions(request):
    userid = User.objects.get(username=User.username).pk
    formRec = ActualQuestions(request.POST or None)

    
    form = QuestionsForm()
    if form.is_valid() :
        form.save()
    context = {
        'form':form
    }
    return render(request,'riskCalculator//questions.html',context)