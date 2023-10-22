from django.db import models
import random
import string
from globalapp2.models import CommonModel, Typess
from projects.models import ProjectInfo
from suppliers.models import Metarials, SupplierBeneficaries
from wearhouse.models import MaterialPurchase

# Create your models here.
# class Brand(CommonModel):
#     name = models.CharField(max_length=30)
#     logo = models.FileField(upload_to='upload')
#     location = models.TextField()

class MaterialDispatch(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    types = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="dispatch_type")
    metarial = models.ManyToManyField(Metarials)
    quantity = models.FloatField()
    unit =  models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="dispatch_unit")


class ProductInventory(MaterialPurchase):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)


