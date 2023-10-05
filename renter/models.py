from django.db import models

from globalapp2.models import Beneficaries, CommonModel
from projects.models import ProjectInfo, propertyModels
from users.models import Employee

# Create your models here.
class RenterBeneficaries(Beneficaries):
    pass

class FlatRent(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    renter_id = models.ForeignKey(RenterBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    advanced_amount = models.FloatField()
    due_amount = models.FloatField()
    def __str__(self):
        return f"{self.property_id.code }"
    
class RentCollection(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    renter_id = models.ForeignKey(RenterBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    rent_amount = models.FloatField()
    due_amount = models.FloatField()
    rent_date = models.DateField()
    def __str__(self):
        return f"{self.property_id.code }"
    

class RepairRecords(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    renter_id = models.ForeignKey(RenterBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    reason = models.TextField()
    amount = models.FloatField()
    OPTION_a = 'Admin'
    OPTION_b = 'Renter'
    
    CHOICES2 = (
        (OPTION_a, 'Admin'),
        (OPTION_b, 'Renter'),
        
        
    )
    
    expensed_by = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    def __str__(self):
        return f"{self.property_id.code }"



