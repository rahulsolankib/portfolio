from django.shortcuts import render

def questions(request):
    return render(request,'riskCalculator/questions.html')