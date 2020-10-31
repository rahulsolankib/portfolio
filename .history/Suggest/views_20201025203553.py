from django.shortcuts import render

def suggest(request):
    students = [{20,12.006750,'CMS'},
{15,10.026,'DFS'},
{8,9.776405,'T'},
{13,6.380289,'ED'},
{3,5.577843,'KO'},
{12,5.536171,'WY'},
{6,5.268869,'ACN'},
{21,4.490807,'AAPL'},
{16,4.033035,'MSFT'},
{9,3.481614,'STX'},
{1,3.430145,'CFG'},
{22,3.317766,'SPG'},
{11,3.262533,'BAX'},
{4,3.151422,'MKC'},
{18,3.113448,'ROST'}
{14,3.043589,'EQR'},
{7,3.018538,'CL'},
{23,2.800363,'PNR'},
{17,2.527764,'EFX'},
{5,2.291049,'SLG'}]
    teachers = [{'id':'1','name':'RJN','Department':'OKAAAY','email':'teacher@gmail.com'}]
    return render(request,'Suggest/suggest.html',{'students':students,'teachers':teachers})