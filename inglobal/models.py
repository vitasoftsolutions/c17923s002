from django.db import models

# Create your models here.
from globalapp2.models import CommonModel
from projects.models import ProjectInfo
from suppliers.models import Metarials, SupplierBeneficaries


class MaterialCommon(CommonModel):
    purchase_for = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    vendor_id = models.ForeignKey(SupplierBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    sr_name = models.CharField(max_length=50,null=True,blank=True)
    sr_number = models.CharField(max_length=50,null=True,blank=True)
    purchase_code = models.CharField(max_length=20, unique=True,null=True,blank=True)
    amount = models.FloatField()
    amount_due = models.FloatField(null=True,blank=True)
    amount_advance = models.FloatField()
    quantity = models.FloatField()
    recieved_quantity = models.FloatField(null=True,blank=True)
    due_quantity = models.FloatField(null=True,blank=True)
    materials = models.ManyToManyField(Metarials,null=True,blank=True)