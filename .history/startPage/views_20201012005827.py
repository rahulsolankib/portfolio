from django.shortcuts import render
from django.http import HttpResponse


details = {'title':'Portfolio Management','founder':'Rahul Solanki'}
def home(request):
    return render(request,'startPage/home.html')

def about(request):
    return render(request,'startPage/about.html')