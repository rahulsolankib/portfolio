from django.shortcuts import render

def suggest(request):
    students = [{'rank':'20','weight':'12.006750','company':'CMS'},
{'rank':'15','weight':'10.026070','company':'DFS'},
{'rank':'8 ','weight':'9.776405','company':'T'},
{'rank':'13','weight':'6.380289','company':'ED'},
{'rank':'3 ','weight':'5.577843 ','company':'KO'},
{'rank':'12','weight':'5.536171','company':'WY'},
{'rank':'6 ','weight':'5.268869 ','company':'ACN'},
{'rank':'21','weight':'4.490807','company':'AAPL'},
{'rank':'16','weight':'4.033035','company':'MSFT'},
{'rank':'9 ','weight':'3.481614 ','company':'STX'},
{'rank':'1 ','weight':'3.430145 ','company':'CFG'},
{'rank':'22','weight':'3.317766','company':'SPG'},
{'rank':'11','weight':'3.262533','company':'BAX'},
{'rank':'4 ','weight':'3.151422 ','company':'MKC'},
{'rank':'18','weight':'3.113448','company':'ROST'},
{'rank':'14','weight':'3.043589','company':'EQR'},
{'rank':'7 ','weight':'3.018538 ','company':'CL'},
{'rank':'23','weight':'2.800363','company':'PNR'},
{'rank':'17','weight':'2.527764','company':'EFX'},
{'rank':'5 ','weight':'2.291049 ','company':'SLG'}]
    sum = 0
    for i in range(len(students)):
        sum += students[i].weights
    return render(request,'Suggest/suggest.html',{'students':students,'teachers':teachers})