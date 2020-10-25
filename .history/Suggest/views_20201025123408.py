from django.shortcuts import render

def suggest(request):
    return render(request,'Suggest/suggest.html')