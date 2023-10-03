from django.db import models
from rest_framework import viewsets
from globalapp2.models import Beneficaries
from datetime import datetime
# Create your models here.
class SupplierBeneficaries(Beneficaries):
    pass

class Metarials(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.JSONField()
    status = models.BooleanField(default=True,null=True,blank=True)
    created_at= models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.name}"


class TestBeneficaries(Beneficaries):
    pass
