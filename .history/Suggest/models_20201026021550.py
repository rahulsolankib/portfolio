from django.db import models

# Create your models here.
class StoreName(models.Model):
    symbol = models.CharField(max_length=120,required=True,unique=True)
    full_name = models.CharField(max_length=120,required=True)