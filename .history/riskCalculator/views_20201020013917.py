from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm

from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    print(formRec['ques2'].value())

    score =( (int(formRec['ques1'].value()) * 25 + int(formRec['ques2'].value()) * 33 + int(formRec['ques3'].value()) * 33 + int(formRec['ques4'].value() * 33) + int(formRec['ques5'].value() * 25) + int(formRec['ques6'].value() * 25 ))/600 )
    userid = request.user.id
    print(type(score))
    
    data = {'userid' : userid, 'risk_score':32}
    form = RiskForm(data)
    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
        print('has')
        
    return render(request,'riskCalculator/questions.html',context)