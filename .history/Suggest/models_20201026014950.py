from django.db import models

# Create your models here.
class StoreName(models.Model):
    symbol = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)