from django.db import models

# Create your models here.
class Questions(models.Model) :
    userid = models.CharField(max_length=120)
    risk_score = models.DecimalField( 
                         max_digits = 2, 
                         decimal_places = 2) 
    
