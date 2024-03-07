from django.db import models
import uuid
from globalapp2.models import CommonModel, Typess
from inglobal.models import MaterialCommon
from inventory.models import ProductInventories


#from inventory.models import ProductInventorys
from projects.models import ProjectInfo
from suppliers.models import Metarials, SupplierBeneficaries
# Create your models here.
####Materials Common

class MaterialPurchases(MaterialCommon):
    def save(self, *args, **kwargs):
        if not self.purchase_code:
            self.purchase_code = str(uuid.uuid4().hex)[:16]
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.purchase_code }"
class WearhouseItem(CommonModel):
    purchase_id = models.ForeignKey(MaterialPurchases,on_delete=models.CASCADE,blank=True,null=True)
    inventory_id = models.ForeignKey(ProductInventories,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.FloatField(blank=True,null=True)
    due_quantity = models.FloatField(blank=True,null=True)
    def __str__(self):
        return f"{self.purchase_id or self.inventory_id }"

class MaterialInstallment(CommonModel):
    purchase_id = models.ForeignKey(MaterialPurchases,on_delete=models.CASCADE,blank=True,null=True)
    recieve_date= models.DateTimeField()
    quantity = models.FloatField()
    type = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.purchase_id.purchase_code }"
    
class WarehouseMaterialDispatch(CommonModel):
    warehouse_item_id = models.ForeignKey(WearhouseItem,on_delete=models.CASCADE,blank=True,null=True)
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    types = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True,related_name="wdispatch_type")
    metarial = models.ManyToManyField(Metarials)
    quantity = models.FloatField()
    unit =  models.ForeignKey(Typess,on_delete= models.CASCADE,blank=True,null=True,related_name="wdispatch_unit")
    OPTION_a = 'Check in'
    OPTION_b = 'Check out'
    
    CHOICES2 = (
        (OPTION_a, 'Check in'),
        (OPTION_b, 'Check out'),  
    )
    
    check_status = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    def __str__(self):
        return f"{self.warehouse_item_id }"
    
class MaterialPaymentinstallment(CommonModel):
    purchase_id = models.ForeignKey(MaterialPurchases,on_delete=models.CASCADE,blank=True,null=True)
    amount = models.FloatField()
    payment_date = models.DateField()
    def __str__(self):
        return f"{self.purchase_id.purchase_code }"


