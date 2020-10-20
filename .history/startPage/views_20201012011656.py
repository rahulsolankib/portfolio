from django.shortcuts import render
from django.http import HttpResponse


details = {'title':'Portfolio Management','founders': ['Rahul Solanki', 'Niti Shah', 'Janice Shah'],'Quote':'Where there is a will there is a way' }
def home(request):
    context = {
        'details' : details,
        'titlae' : 'Portolio Management'
    }
    return render(request,'startPage/home.html',context)

def about(request):
    return render(request,'startPage/about.html')