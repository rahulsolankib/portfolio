from django.shortcuts import render
import yfinance as yf 
from riskCalculator.models import RiskModel
from Suggest.models import StoreName  

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
        companies = [ {'rank':' 6','weight':  '7.648189'   ,'company':'  ACN'},
{'rank':'21','weight':  '7.609613'   ,'company':'MLM'},
{'rank':'12','weight':  '6.786549'   ,'company':'USB'},
{'rank':' 2','weight':  '6.528445'   ,'company':'BLL'},
{'rank':' 4','weight':  '5.734195'   ,'company':'CMI'},
{'rank':' 5','weight':  '5.685196'   ,'company':'DG'},
{'rank':'11','weight':  '5.407029'   ,'company':'TEL'},
{'rank':'18','weight':  '5.324783'   ,'company':'CMCSA'},
{'rank':' 7','weight':  '5.015832'   ,'company':'SRE'},
{'rank':'10','weight':  '4.916086'   ,'company':'OKE'},
{'rank':'15','weight':  '4.794459'   ,'company':'DFS'},
{'rank':'17','weight':  '4.651321'   ,'company':'HBAN'},
{'rank':'22','weight':  '4.360461'   ,'company':'CAG'},
{'rank':' 1','weight':  '3.333384'   ,'company':'COP'},
{'rank':'23','weight':  '3.189468'   ,'company':'WMT'},
{'rank':' 9','weight':  '3.181557'   ,'company':'SNPS'},
{'rank':'19','weight':  '3.060298'   ,'company':'NWSA'},
{'rank':'16','weight':  '2.838206'   ,'company':'HIG'},
{'rank':'20','weight':  '2.728589'   ,'company':'CMS'},
{'rank':'13','weight':  '2.371006'   ,'company':'KLAC'}]
    elif(score>60 and score<=80):
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
    else :
       companies = [{'rank':'17',  'weight':'14.743481', 'company':'HBAN'},
{'rank':' 5','weight':  '10.209154','company':'NAVI'},
{'rank':'13','weight':  ' 6.338018','company':'VMC'},
{'rank':' 6','weight':  ' 6.076180','company':'CMG'},
{'rank':' 2','weight':  ' 5.921661','company':'ADM'},
{'rank':' 9','weight':  ' 5.649694','company':'LEN'},
{'rank':'14','weight':  ' 5.629875','company':'SRCL'},
{'rank':'22','weight':  ' 5.403317','company':'CAG'},
{'rank':' 4','weight':  ' 4.679148','company':'AVY'},
{'rank':'16','weight':  ' 4.317574','company':'K'},
{'rank':'12','weight':  ' 3.658119','company':'FDX'},
{'rank':'23','weight':  ' 3.627833','company':'LMT'},
{'rank':'11','weight':  ' 3.526781','company':'TRV'},
{'rank':'10','weight':  ' 2.964144','company':'LKQ'},
{'rank':'19','weight':  ' 2.660496','company':'MPC'},
{'rank':' 7','weight':  ' 2.299644','company':'URI'},
{'rank':'15','weight':  ' 2.216550','company':'PCG'},
{'rank':'8 ','weight':  '2.101344 ','company': 'HRB'},
{'rank':'1 ','weight':  '1.909679 ','company': 'ZTS'},
{'rank':'20','weight':  ' 1.830676','company':'DIS'}]


    comp1 = [{'rank':'20','weight':'12.006750','company':'CMS'},
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



    comp2 = [{'rank':'6' , 'weight':'20.378874' ,'company': 'SO'},    
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


    comp3 = [{'rank':' 6','weight':  '7.648189'   ,'company':'ACN'},
    {'rank':'21','weight':  '7.609613'   ,'company':'MLM'},
    {'rank':'12','weight':  '6.786549'   ,'company':'USB'},
    {'rank':' 2','weight':  '6.528445'   ,'company':'BLL'},
    {'rank':' 4','weight':  '5.734195'   ,'company':'CMI'},
    {'rank':' 5','weight':  '5.685196'   ,'company':'DG'},
    {'rank':'11','weight':  '5.407029'   ,'company':'TEL'},
    {'rank':'18','weight':  '5.324783'   ,'company':'CMCSA'},
    {'rank':' 7','weight':  '5.015832'   ,'company':'SRE'},
    {'rank':'10','weight':  '4.916086'   ,'company':'OKE'},
    {'rank':'15','weight':  '4.794459'   ,'company':'DFS'},
    {'rank':'17','weight':  '4.651321'   ,'company':'HBAN'},
    {'rank':'22','weight':  '4.360461'   ,'company':'CAG'},
    {'rank':' 1','weight':  '3.333384'   ,'company':'COP'},
    {'rank':'23','weight':  '3.189468'   ,'company':'WMT'},
    {'rank':' 9','weight':  '3.181557'   ,'company':'SNPS'},
    {'rank':'19','weight':  '3.060298'   ,'company':'NWSA'},
    {'rank':'16','weight':  '2.838206'   ,'company':'HIG'},
    {'rank':'20','weight':  '2.728589'   ,'company':'CMS'},
    {'rank':'13','weight':  '2.371006'   ,'company':'KLAC'}]

    comp4 = [{'rank':'17',  'weight':'14.743481', 'company':'HBAN'},
    {'rank':' 5','weight':  '10.209154','company':'NAVI'},
    {'rank':'13','weight':  ' 6.338018','company':'VMC'},
    {'rank':' 6','weight':  ' 6.076180','company':'CMG'},
    {'rank':' 2','weight':  ' 5.921661','company':'ADM'},
    {'rank':' 9','weight':  ' 5.649694','company':'LEN'},
    {'rank':'14','weight':  ' 5.629875','company':'SRCL'},
    {'rank':'22','weight':  ' 5.403317','company':'CAG'},
    {'rank':' 4','weight':  ' 4.679148','company':'AVY'},
    {'rank':'16','weight':  ' 4.317574','company':'K'},
    {'rank':'12','weight':  ' 3.658119','company':'FDX'},
    {'rank':'23','weight':  ' 3.627833','company':'LMT'},
    {'rank':'11','weight':  ' 3.526781','company':'TRV'},
    {'rank':'10','weight':  ' 2.964144','company':'LKQ'},
    {'rank':'19','weight':  ' 2.660496','company':'MPC'},
    {'rank':' 7','weight':  ' 2.299644','company':'URI'},
    {'rank':'15','weight':  ' 2.216550','company':'PCG'},
    {'rank':'8 ','weight':  '2.101344 ','company': 'HRB'},
    {'rank':'1 ','weight':  '1.909679 ','company': 'ZTS'},
    {'rank':'20','weight':  ' 1.830676','company':'DIS'}]
    def fullName(shortname):
        name = yf.Ticker(shortname)
        return name.info['longName'] 
    for ele in comp3:
        symbol= ele['company']
        full_name = fullName(symbol)
        StoreName.objects.create(symbol=symbol, full_name=full_name)

    return render(request,'Suggest/suggest.html',{'companies':companies})


     