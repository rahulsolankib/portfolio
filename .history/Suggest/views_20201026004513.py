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
        companies = [{'17',  '14.743481',    'HBAN'},
{' 5',  '10.209154',    'NAVI'},
{'13',  ' 6.338018',    ' VMC'},
{' 6',  ' 6.076180',    ' CMG'},
{' 2',  ' 5.921661',    ' ADM'},
{' 9',  ' 5.649694',    ' LEN'},
{'14',  ' 5.629875',    'SRCL'},
{'22',  ' 5.403317',    ' CAG'},
{' 4',  ' 4.679148',    ' AVY'},
{'16',  ' 4.317574',    '   K'},
{'12',  ' 3.658119',    ' FDX'},
{'23',  ' 3.627833',    ' LMT'},
{'11',  ' 3.526781',    ' TRV'},
{'10',  ' 2.964144',    ' LKQ'},
{'19',  ' 2.660496',    ' MPC'},
{' 7',  ' 2.299644',    ' URI'},
{'15',  ' 2.216550',    ' PCG'},
{'8 ',  '2.101344 ',     'HRB'},
{'1 ',  '1.909679 ',     'ZTS'},
{'20',  ' 1.830676',    ' DIS'}]


    
    return render(request,'Suggest/suggest.html',{'companies':[]})