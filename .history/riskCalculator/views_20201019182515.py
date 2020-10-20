from django.shortcuts import render
from .forms import QueForm

from .models import RiskModel

def questions(request):
    formRec = QueForm(request.POST)
    context = {
        'formRec': formRec
    }
    return render(request,'riskCalculator/questions.html',context)