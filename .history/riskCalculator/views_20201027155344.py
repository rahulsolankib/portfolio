  
from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm
from django.contrib import messages
from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    # print(formRec['ques5'].value())
    if request.method == 'POST':
        score =(((int(formRec['ques1'].value()) * 25 + int(formRec['ques2'].value()) * 33 + int(formRec['ques4'].value()) * 33 + int(formRec['ques5'].value()) * 25+ int(formRec['ques6'].value()) * 25))/500)
        userid = request.user.id
        print(score)
        data = {'userid' : userid, 'risk_score':(score * 100)}
        form = RiskForm(data)
        if form.is_valid():
            print('has')
            profile = form.save(commit=False)
            profile.user = request.user 
            profile.save()
            return render(request,'riskCalculator/questions.html',context)

    return render(request,'riskCalculator/questions.html',context)
