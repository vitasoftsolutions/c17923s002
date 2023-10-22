from django.db import models
import uuid
from globalapp2.models import CommonModel, Typess
from projects.models import ProjectInfo
from suppliers.models import Metarials, SupplierBeneficaries
# Create your models here.
class MaterialPurchase(CommonModel):
    purchase_for = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    vendor_id = models.ForeignKey(SupplierBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    sr_name = models.CharField(max_length=50,null=True,blank=True)
    sr_number = models.CharField(max_length=50,null=True,blank=True)
    purchase_code = models.CharField(max_length=20, unique=True,null=True,blank=True)
    amount = models.FloatField()
    amount_due = models.FloatField()
    amount_advance = models.FloatField()
    quantity = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.purchase_code:
            self.purchase_code = str(uuid.uuid4().hex)[:16]
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.purchase_code }"


class MaterialInstallment(CommonModel):
    purchase_id = models.ForeignKey(MaterialPurchase,on_delete=models.CASCADE,blank=True,null=True)
    recieve_date= models.DateTimeField()
    quantity = models.FloatField()
    type = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.purchase_id.purchase_code }"


