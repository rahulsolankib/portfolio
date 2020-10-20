from django.shortcuts import render

# Create your views here.
def questions(request):
    return render(request,'riskCalculator\questions.html')