from django.shortcuts import render
from .models import Questions
from .forms import QuestionsForm    
# Create your views here.
def questions(request):
    form = QuestionsForm()
    return render(request,'riskCalculator//questions.html')