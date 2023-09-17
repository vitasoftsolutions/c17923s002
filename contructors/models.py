from django.db import models

from globalapp2.models import Beneficaries, IntroInfo

# Create your models here.
class ContructorsBeneficaries(Beneficaries):
    pass
class ContractorGarrentor(IntroInfo):
    role = models.CharField(max_length=100)
    contractor_id= models.ForeignKey(ContructorsBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
