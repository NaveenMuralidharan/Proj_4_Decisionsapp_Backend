from django.db import models

# Create your models here.
class Decision(models.Model):
    regBody         = models.CharField(max_length=100)
    companyName     = models.CharField(max_length=100)
    decisionType    = models.CharField(max_length=100)
    allegationType  = models.CharField(max_length=100)