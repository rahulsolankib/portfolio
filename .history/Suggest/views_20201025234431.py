from django.shortcuts import render
import yfinance as yf 
from riskCalculator.models import RiskModel

def fullName(shortname):
    name = yf.Ticker(shortname)
    return name.info['longName'] 
def suggest(request):
    entry = RiskModel.objects.get(userid=9)
    print(entry)
#     companies = [{'rank':'20','weight':'12.006750','company':fullName('CMS')},
# {'rank':'15','weight':'10.026070','company':fullName('DFS')},
# {'rank':'8 ','weight':'9.776405','company':fullName('T')},
# {'rank':'13','weight':'6.380289','company':fullName ('ED'  )},
# {'rank':'3 ','weight':'5.577843 ','company':fullName('KO'  )},
# {'rank':'12','weight':'5.536171','company':fullName ('WY'  )},
# {'rank':'6 ','weight':'5.268869 ','company':fullName('ACN' )},
# {'rank':'21','weight':'4.490807','company':fullName ('AAPL')},
# {'rank':'16','weight':'4.033035','company':fullName ('MSFT')},
# {'rank':'9 ','weight':'3.481614 ','company':fullName('STX' )},
# {'rank':'1 ','weight':'3.430145 ','company':fullName('CFG' )},
# {'rank':'22','weight':'3.317766','company':fullName ('SPG' )},
# {'rank':'11','weight':'3.262533','company':fullName ('BAX' )},
# {'rank':'4 ','weight':'3.151422 ','company':fullName('MKC' )},
# {'rank':'18','weight':'3.113448','company':fullName ('ROST')},
# {'rank':'14','weight':'3.043589','company':fullName('EQR')},
# {'rank':'7 ','weight':'3.018538 ','company':fullName('CL')},
# {'rank':'23','weight':'2.800363','company':fullName('PNR')},
# {'rank':'17','weight':'2.527764','company':fullName('EFX')},
# {'rank':'5 ','weight':'2.291049 ','company':fullName('SLG')}]
    sum = 0
    
    return render(request,'Suggest/suggest.html',{'companies':[]})