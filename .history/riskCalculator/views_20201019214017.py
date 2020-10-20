from django.shortcuts import render
from .forms import QueForm,RiskForm

from .models import RiskModel

def questions(request):
    formRec = QueForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    data = {'id' : 1, 'risk_score':20}
    form = RiskForm(data)

    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
    return render(request,'riskCalculator/questions.html',context)