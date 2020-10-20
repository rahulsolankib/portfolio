from django.shortcuts import render
from .forms import QueForm

from .models import RiskModel

def questions(request):
    formRec = QueForm(request.POST)
    context = {
        'formRec': formRec
    }
    data = {'id' : 1, 'risk_score':20}
    form = RiskModel(data)

    form.save()
    return render(request,'riskCalculator/questions.html',context)