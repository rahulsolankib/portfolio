from django.db import models

# Create your models here.
class Questions(models.Model) :
    userid = models.CharField(max_length=120)
    risk_score = models.DecimalField( 
                         max_digits = 5, 
                         decimal_places = 2) 
    
class Actual(models.Model):
    ques1 = models.CharField(max_length=120)
    ques2 = models.CharField(max_length=120)
    ques3 = models.CharField(max_length=120)
    ques4 = models.CharField(max_length=120)
    ques5 = models.CharField(max_length=120)
    