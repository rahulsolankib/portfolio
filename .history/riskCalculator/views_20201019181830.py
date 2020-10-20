from django.shortcuts import render
from .forms import QueForm

def questions(request):
    formRec = QueForm
    context = {
        'formRec': formRec
    }
    return render(request,'riskCalculator/questions.html',formRec)