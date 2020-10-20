from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm

from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    print(formRec['ques5'].value())

    score =(int(formRec['ques1'].value()) + int(formRec['ques2'].value())+ int(formRec['ques3'].value())+ int(formRec['ques4'].value()) + int(formRec['ques5'].value()) + int(formRec['ques6'].value()))
    userid = request.user.id
    print(formRec['ques6'].value())
    
    data = {'userid' : userid, 'risk_score':32}
    form = RiskForm(data)
    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
        print('has')
        
    return render(request,'riskCalculator/questions.html',context)