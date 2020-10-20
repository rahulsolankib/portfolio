from django.shortcuts import render
from .models import Questions
from .forms import QuestionsForm as form
# Create your views here.
def questions(request):
    return render(request,'riskCalculator//questions.html')