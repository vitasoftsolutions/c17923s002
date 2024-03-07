from django.db import models
from rest_framework import viewsets
from globalapp2.models import Beneficaries, CommonModel, Typess
from datetime import datetime

from django.apps import apps

#from inventory.models import Brand
# Create your models here.
#Brand = apps.get_model('inventory', 'Brand')
class Brands(CommonModel):
    name = models.CharField(max_length=30)
    logo = models.FileField(upload_to='upload')
    location = models.TextField()
    def __str__(self):
        return f"{self.name }"
class SupplierBeneficaries(Beneficaries):
    brand = models.ManyToManyField(Brands,null=True,blank=True)
    

class Metarials(models.Model):
    type = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="materials_type")
    name = models.CharField(max_length=100)
    description = models.TextField()
    features = models.JSONField()
    brand = models.ManyToManyField(Brands,null=True,blank=True)
    dimenssion = models.FloatField(null=True,blank=True)
    unit = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="materials_unit")
    status = models.BooleanField(default=True,null=True,blank=True)
    created_at= models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.name}"



