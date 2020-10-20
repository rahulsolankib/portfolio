from django.shortcuts import render
from forms import questions

def questions(request):
    
    return render(request,'riskCalculator/questions.html')