from django.db import models

from globalapp2.models import Beneficaries, CommonModel, IntroInfo, Typess
from projects.models import ProjectInfo

# Create your models here.
class ContructorsBeneficaries(Beneficaries):
    pass
class ContractorGarrentor(IntroInfo):
    role = models.CharField(max_length=100)
    contractor_id= models.ForeignKey(ContructorsBeneficaries,on_delete=models.CASCADE,blank=True,null=True)


class AssignContractor(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    contructor_id = models.ForeignKey(ContructorsBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    rate = models.FloatField()
    rate_per_work = models.FloatField()
    unit = models.IntegerField()
    work_order_amount = models.FloatField()
    payed_amount = models.FloatField()
    due_amount = models.FloatField()
    workers = models.IntegerField()
    worker_payement = models.FloatField()
    security_money_percentage = models.FloatField()
    security_amount = models.FloatField()

    def __str__(self):
        return f"{self.project_id.name}"
    
class ContractorPaymnet(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    contructor_id = models.ForeignKey(ContructorsBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    worker = models.IntegerField()
    payment = models.FloatField()
    payment_type = models.ForeignKey(Typess,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.project_id.name}"