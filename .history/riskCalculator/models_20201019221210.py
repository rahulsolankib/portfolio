from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Que(models.Model):
    ques1 = models.CharField(max_length=120)
    ques2 = models.CharField(max_length=120)
    ques3 = models.CharField(max_length=120)
    ques4 = models.CharField(max_length=120)
    ques5 = models.CharField(max_length=120)

class RiskModel(models.Model):
    userid = models.IntegerField()
    userid = models.ForeignKey(,default=1,on_delete=models.SET_DEFAULT)
    risk_score = models.DecimalField( 
                         max_digits = 5, 
                         decimal_places = 2)
