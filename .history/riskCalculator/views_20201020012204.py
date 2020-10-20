from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm

from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    print(formRec['ques1'].value())
    userid = request.user.id


    data = {'userid' : userid, 'risk_score':32}
    form = RiskForm(data)
    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
        
    return render(request,'riskCalculator/questions.html',context)