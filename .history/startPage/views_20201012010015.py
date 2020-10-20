from django.shortcuts import render
from django.http import HttpResponse


details = {'title':'Portfolio Management','founder': ['Rahul Solanki, Niti Shah, Janice Shah'],'Quote':'Where there is a will there is a way' }
def home(request):
    context = {
        'details' : details
    }
    return render(request,'startPage/home.html')

def about(request):
    return render(request,'startPage/about.html')