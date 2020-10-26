from django.shortcuts import render
import yfinance as yf 
from riskCalculator.models import RiskModel
from Suggest.models import StoreName  

# def fullName(shortname):
#     name = yf.Ticker(shortname)
#     return name.info['longName'] 
def suggest(request):
    entry = RiskModel.objects.filter(userid=request.user.id)
    fullname = StoreName.objects
    score = getattr(entry.last(),'risk_score')
    # print('suggest ',score)
    if(score>29 and score<=40):
        company_sym = ['CMS', 'DFS', 'T', 'ED', 'KO', 'WY', 'ACN', 'AAPL', 'MSFT', 'STX', 'CFG', 'SPG', 'BAX', 'MKC', 'ROST', 'EQR', 'CL', 'PNR', 'EFX', 'SLG']
        fullname_list = []
        for i in company_sym:
            fullname_list.append(getattr(fullname.filter(symbol=company_sym[i])[0],'full_name'))

        companies = [{'rank':'20','weight':'12.006750','company':fullname_list[0]},
{'rank':'15','weight':'10.026070','company':fullname_list[1] },
{'rank':'8 ','weight':'9.776405','company' :fullname_list[2] },
{'rank':'13','weight':'6.380289','company' :fullname_list[3] },
{'rank':'3 ','weight':'5.577843 ','company':fullname_list[4] },
{'rank':'12','weight':'5.536171','company' :fullname_list[5] },
{'rank':'6 ','weight':'5.268869 ','company':fullname_list[6] },
{'rank':'21','weight':'4.490807','company' :fullname_list[7] },
{'rank':'16','weight':'4.033035','company' :fullname_list[8] },
{'rank':'9 ','weight':'3.481614 ','company':fullname_list[9] },
{'rank':'1 ','weight':'3.430145 ','company':fullname_list[10] },
{'rank':'22','weight':'3.317766','company' :fullname_list[11] },
{'rank':'11','weight':'3.262533','company' :fullname_list[12] },
{'rank':'4 ','weight':'3.151422 ','company':fullname_list[13] },
{'rank':'18','weight':'3.113448','company' :fullname_list[14] },
{'rank':'14','weight':'3.043589','company' :fullname_list[15] },
{'rank':'7 ','weight':'3.018538 ','company':fullname_list[16] },
{'rank':'23','weight':'2.800363','company' :fullname_list[17] },
{'rank':'17','weight':'2.527764','company' :fullname_list[18] },
{'rank':'5 ','weight':'2.291049 ','company':fullname_list[19] }]
    elif(score>40 and score<=60):
        company_sym = ['SO','PPG','NAVI','PH','HAL','HBAN','NEM','D','AME','LKQ','FB','ROP','EXPD','COP','LEN','ADI','XRX','CAG','SWK','PYPL',]
        fullname_list = []
        for i in company_sym:
            fullname_list.append(getattr(fullname.filter(symbol=company_sym[i])[0],'full_name'))
        companies = [ {'rank':' 6','weight':  '7.648189'   ,'company':fullname_list[0] },
{'rank':'21','weight':  '7.609613'   ,'company':fullname_list[1] },
{'rank':'12','weight':  '6.786549'   ,'company':fullname_list[2] },
{'rank':' 2','weight':  '6.528445'   ,'company':fullname_list[3] },
{'rank':' 4','weight':  '5.734195'   ,'company':fullname_list[4] },
{'rank':' 5','weight':  '5.685196'   ,'company':fullname_list[5] },
{'rank':'11','weight':  '5.407029'   ,'company':fullname_list[6] },
{'rank':'18','weight':  '5.324783'   ,'company':fullname_list[7] },
{'rank':' 7','weight':  '5.015832'   ,'company':fullname_list[8] },
{'rank':'10','weight':  '4.916086'   ,'company':fullname_list[9] },
{'rank':'15','weight':  '4.794459'   ,'company':fullname_list[10]},
{'rank':'17','weight':  '4.651321'   ,'company':fullname_list[11]},
{'rank':'22','weight':  '4.360461'   ,'company':fullname_list[12]},
{'rank':' 1','weight':  '3.333384'   ,'company':fullname_list[13]},
{'rank':'23','weight':  '3.189468'   ,'company':fullname_list[14]},
{'rank':' 9','weight':  '3.181557'   ,'company':fullname_list[15]},
{'rank':'19','weight':  '3.060298'   ,'company':fullname_list[16]},
{'rank':'16','weight':  '2.838206'   ,'company':fullname_list[17]},
{'rank':'20','weight':  '2.728589'   ,'company':fullname_list[18]},
{'rank':'13','weight':  '2.371006'   ,'company':fullname_list[19]}]
    elif(score>60 and score<=80):
        company_list_sym = ['SO','PPG',]
        companies = [{'rank':'6' , 'weight':'20.378874' ,'company': fullname_list[0]},    
{'rank':'15','weight':  ' 7.744627','company':fullname_list[1] },
{'rank':'5' ,'weight': ' 7.121672' ,'company':fullname_list[2] },
{'rank':'13','weight':  ' 5.507530','company':fullname_list[3] },
{'rank':'2' ,'weight': ' 5.310478' ,'company':fullname_list[4] },
{'rank':'17','weight':  ' 4.875722','company':fullname_list[5] },
{'rank':'16','weight':  ' 4.301703','company':fullname_list[6] },
{'rank':'18','weight':  ' 4.198316','company':fullname_list[7] },
{'rank':'12','weight':  ' 4.010637','company':fullname_list[8] },
{'rank':'10','weight':  ' 3.642967','company':fullname_list[9] },
{'rank':'20','weight':  ' 3.483489','company':fullname_list[10]},
{'rank':'23','weight':  ' 3.476323','company':fullname_list[11]},
{'rank':'11','weight':  ' 3.317969','company':fullname_list[12]},
{'rank':'1' ,'weight': ' 3.255640' ,'company':fullname_list[13]},
{'rank':'9' ,'weight': ' 2.839934' ,'company':fullname_list[14]},
{'rank':'7' ,'weight': ' 2.787716' ,'company':fullname_list[15]},
{'rank':'19','weight':  ' 2.587637','company':fullname_list[16]},
{'rank':'22','weight':  ' 2.527337','company':fullname_list[17]},
{'rank':'21','weight':  ' 2.267334','company':fullname_list[18]},
{'rank':'8' ,'weight': ' 2.045686' ,'company':fullname_list[19]}]
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


    return render(request,'Suggest/suggest.html',{'companies':companies})


     