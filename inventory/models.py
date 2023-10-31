from django.db import models
import random
import string

from globalapp2.models import CommonModel, Typess
from inglobal.models import MaterialCommon
from projects.models import ProjectInfo
from suppliers.models import Metarials, SupplierBeneficaries

#from wearhouse.models import MaterialCommon

# Create your models here.
# class Brand(CommonModel):
#     name = models.CharField(max_length=30)
#     logo = models.FileField(upload_to='upload')
#     location = models.TextField()
class ProductInventories(MaterialCommon):
    use_quantity = models.FloatField(blank=True,null=True)
    def __str__(self):
        return f"{self.purchase_for.name }"
class MaterialDispatch(CommonModel):
    inventory_item_id = models.ForeignKey(ProductInventories,on_delete=models.CASCADE,blank=True,null=True)
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    types = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="dispatch_type")
    metarial = models.ManyToManyField(Metarials)
    quantity = models.FloatField()
    unit =  models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="dispatch_unit")
    OPTION_a = 'Check in'
    OPTION_b = 'Check out'
    OPTION_c = 'Return'
    OPTION_d = 'Swap'
    
    CHOICES2 = (
        (OPTION_a, 'Check in'),
        (OPTION_b, 'Check out'),
        (OPTION_c, 'Return'), 
        (OPTION_d, 'Swap'),     
    )
    
    check_status = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    def __str__(self):
        return f"{self.inventory_item_id }"


