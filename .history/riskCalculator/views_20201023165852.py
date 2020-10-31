from django.shortcuts import render
from .forms import QueForm,RiskForm,QForm
from twilio.rest import Client 

from .models import RiskModel

def questions(request):
    formRec = QForm(request.POST or None)
    context = {
        'formRec': formRec
    }
    # print(formRec['ques5'].value())

    score =(((int(formRec['ques1'].value()) * 25 + int(formRec['ques2'].value()) * 33 + int(formRec['ques3'].value()) * 33 + int(formRec['ques4'].value()) * 33 + int(formRec['ques5'].value()) * 25+ int(formRec['ques6'].value()) * 25))/600)
    userid = request.user.id
    print(score)
    
    data = {'userid' : userid, 'risk_score':(score * 100)}
    form = RiskForm(data)
    if form.is_valid(): 
        account_sid = 'AC99c04c65707246fda97538520277b450' 
        auth_token = '190674744f34baa4078fb2325dcbb6fc' 
        client = Client(account_sid, auth_token) 
        
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Your appointment is coming up on July 21 at 3PM',      
                                    to='whatsapp:+919930414832' 
                                ) 
        
        print(message.sid)
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        print('has')
        
    return render(request,'riskCalculator/questions.html',context)