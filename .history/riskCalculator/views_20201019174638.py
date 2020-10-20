from django.shortcuts import render
from .models import Questions
from .forms import QuestionsForm    
# Create your views here.
def questions(request):
    form = QuestionsForm()
    if form.is_valid() :
        form.save()
    context = {
        'form':form
    }
    return render(request,'riskCalculator//questions.html',context)