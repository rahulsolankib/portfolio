from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm

from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    print(formRec['ques2'].value())

    score =( (formRec['ques1'].value() * 25 + formRec['ques2'].value() * 33 + formRec['ques3'].value() * 33 + formRec['ques4'].value() * 33 + formRec['ques5'].value() * 25 + formRec['ques6'].value() * 25 ) / 6 )
    userid = request.user.id


    data = {'userid' : userid, 'risk_score':score}
    form = RiskForm(data)
    if form.is_valid():
        profile = form.save(commit = True)
        profile.user = request.user
        profile.save()
        
    return render(request,'riskCalculator/questions.html',context)