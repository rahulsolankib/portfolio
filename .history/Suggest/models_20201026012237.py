from django.db import models

# Create your models here.
def StoreName(models.Model):
    userid = models.CharField(max_length=120)
    risk_score = models.CharField(max_length=120)