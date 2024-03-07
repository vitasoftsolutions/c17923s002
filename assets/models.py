from django.db import models

from globalapp2.models import CommonModel, Typess

# Create your models here.
class AssetsListing(CommonModel):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    depriciation_amount = models.CharField(max_length=100)
    depriciation_type = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True)
    current_price = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}"
    

class AssetsSell(CommonModel):
    name = models.ForeignKey(AssetsListing,on_delete=models.CASCADE,blank=True,null=True)
    buyer_name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    buyer_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    file = models.FileField()
    date = models.DateField()
    


    def __str__(self):
        return f"{self.name}"