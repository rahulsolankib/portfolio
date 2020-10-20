from django.shortcuts import render
from .forms import QueForm

def questions(request):
    formRec = QueForm
    return render(request,'riskCalculator/questions.html')