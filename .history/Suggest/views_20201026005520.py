from django.shortcuts import render
import yfinance as yf 
from riskCalculator.models import RiskModel

def fullName(shortname):
    name = yf.Ticker(shortname)
    return name.info['longName'] 
def suggest(request):
    entry= RiskModel.objects.filter(userid=request.user.id)
    score = getattr(entry.last(),'risk_score')
    # print('suggest ',score)
    if(score>29 and score<=40):
        companies = [{'rank':'20','weight':'12.006750','company':'CMS'},
{'rank':'15','weight':'10.026070','company':'DFS'},
{'rank':'8 ','weight':'9.776405','company' :'T'},
{'rank':'13','weight':'6.380289','company' :'ED'  },
{'rank':'3 ','weight':'5.577843 ','company':'KO'  },
{'rank':'12','weight':'5.536171','company' :'WY'  },
{'rank':'6 ','weight':'5.268869 ','company':'ACN' },
{'rank':'21','weight':'4.490807','company' :'AAPL'},
{'rank':'16','weight':'4.033035','company' :'MSFT'},
{'rank':'9 ','weight':'3.481614 ','company':'STX' },
{'rank':'1 ','weight':'3.430145 ','company':'CFG' },
{'rank':'22','weight':'3.317766','company' :'SPG' },
{'rank':'11','weight':'3.262533','company' :'BAX' },
{'rank':'4 ','weight':'3.151422 ','company':'MKC' },
{'rank':'18','weight':'3.113448','company' :'ROST'},
{'rank':'14','weight':'3.043589','company' :'EQR'},
{'rank':'7 ','weight':'3.018538 ','company':'CL'},
{'rank':'23','weight':'2.800363','company' :'PNR'},
{'rank':'17','weight':'2.527764','company' :'EFX'},
{'rank':'5 ','weight':'2.291049 ','company':'SLG'}]
    elif(score>40 and score<=60):
        companies = [{'rank':'6' , 'weight':'20.378874' ,'company': 'SO'},    
{'rank':'15','weight':  ' 7.744627','company':   'PPG'},
{'rank':'5' ,'weight': ' 7.121672' ,'company':  'NAVI'},
{'rank':'13','weight':  ' 5.507530','company':    'PH'},
{'rank':'2' ,'weight': ' 5.310478' ,'company':   'HAL'},
{'rank':'17','weight':  ' 4.875722','company':  'HBAN'},
{'rank':'16','weight':  ' 4.301703','company':   'NEM'},
{'rank':'18','weight':  ' 4.198316','company':     'D'},
{'rank':'12','weight':  ' 4.010637','company':   'AME'},
{'rank':'10','weight':  ' 3.642967','company':   'LKQ'},
{'rank':'20','weight':  ' 3.483489','company':    'FB'},
{'rank':'23','weight':  ' 3.476323','company':   'ROP'},
{'rank':'11','weight':  ' 3.317969','company':  'EXPD'},
{'rank':'1' ,'weight': ' 3.255640' ,'company':   'COP'},
{'rank':'9' ,'weight': ' 2.839934' ,'company':   'LEN'},
{'rank':'7' ,'weight': ' 2.787716' ,'company':   'ADI'},
{'rank':'19','weight':  ' 2.587637','company':   'XRX'},
{'rank':'22','weight':  ' 2.527337','company':   'CAG'},
{'rank':'21','weight':  ' 2.267334','company':   'SWK'},
{'rank':'8' ,'weight': ' 2.045686' ,'company':  'PYPL'}]
    elif(score>60 and score<=80):
        companies = 

return render(request,'Suggest/suggest.html',{'companies':companies})