from django.db import models

# Create your models here.
class Que(models.Model):
    ques1 = models.CharField(max_length=120)
    ques2 = models.CharField(max_length=120)
    ques3 = models.CharField(max_length=120)
    ques4 = models.CharField(max_length=120)
    ques5 = models.CharField(max_length=120)
