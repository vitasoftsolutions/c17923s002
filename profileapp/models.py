from django.db import models

from globalapp2.models import CommonModel,PhoneNumber

# Create your models here.
class BusinessProfile(CommonModel):
    name= models.CharField(max_length=100,blank=True,null=True)
    logo = models.FileField(upload_to="logo")
    address = models.TextField()
    phone_number = models.ManyToManyField(PhoneNumber,null=True,blank=True)
    license_number = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"