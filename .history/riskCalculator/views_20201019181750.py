from django.shortcuts import render
from .forms import QueForm

def questions(request):
    
    return render(request,'riskCalculator/questions.html')