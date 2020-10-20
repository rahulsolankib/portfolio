from django.shortcuts import render
from .forms import QueForm,RiskForm

from .models import RiskModel

def questions(request):
    formRec = QueForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    
    data = {'userid' : 1, 'risk_score':30}
    form = RiskForm(data)
    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
        print(profile.username)
        
    return render(request,'riskCalculator/questions.html',context)