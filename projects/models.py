from django.db import models
from customers.models import CustomerBeneficaries

from globalapp2.models import CommonModel, Types
from users.models import Employee

# Create your models here.
class ProjectInfo(CommonModel):
    name= models.CharField(max_length=100,blank=True,null=True)
    project_type = models.ForeignKey(Types,on_delete=models.CASCADE,related_name='project_type',blank=True,null=True)
    address = models.TextField()
    area= models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    city_corporation = models.CharField(max_length=20)
    ward_no = models.CharField(max_length=20)
    post_office = models.CharField(max_length=20)
    police_station = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    project_size = models.FloatField()
    project_size_type = models.ForeignKey(Types,on_delete=models.CASCADE,related_name='project_size_type',blank=True,null=True)
    basement_no = models.IntegerField()
    number_of_elevator = models.IntegerField()
    number_of_stairs = models.IntegerField()
    number_of_parking = models.IntegerField()
    number_of_shops = models.IntegerField()
    #join_venture_spliting_ratio = 
    work_start_date = models.DateField()
    expected_handover_date= models.DateField()
    commarcial_floor = models.IntegerField()
    commarcial_unit = models.IntegerField()
    residential_floor = models.IntegerField()
    residential_unit= models.IntegerField()
    def __str__(self):
        return f"{self.name}"
    
class WorkProgress(CommonModel):
    name = models.CharField(max_length=20)
    percentage = models.FloatField()
    def __str__(self):
        return f"{self.name}"
    
class projectProgress(CommonModel):
    wp_ids = models.ManyToManyField(WorkProgress)
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    note = models.TextField()
    def __str__(self):
        return f"{self.note}"
    

class propertyModels(CommonModel):
    code = models.CharField(max_length=10)


class propertyPurchase(CommonModel):
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    customer_id = models.ForeignKey(CustomerBeneficaries,on_delete=models.CASCADE,blank=True,null=True)
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    amount = models.FloatField()
    payment_type = models.ForeignKey(Types,on_delete=models.CASCADE,blank=True,null=True)
    down_payment = models.FloatField()
    installment = models.IntegerField()
    facilities = models.JSONField()
    installment_duration = models.IntegerField()
    final_return= models.DateField()
    due_amount = models.FloatField()
    due_installment = models.FloatField()
    handover_status = models.BooleanField()
    def __str__(self):
        return f"{self.property_id.code }"

class propertyInstallment(CommonModel):
    purchase_id = models.ForeignKey(propertyPurchase,on_delete=models.CASCADE)
    amount = models.FloatField()
    installment_date= models.DateField()
    project_id = models.ForeignKey(ProjectInfo,on_delete=models.CASCADE,blank=True,null=True)
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.property_id.code }"
    
class ExpenseByProperty(CommonModel):
    property_id = models.ForeignKey(propertyModels,on_delete=models.CASCADE,blank=True,null=True)
    reason = models.TextField()
    type = models.ForeignKey(Types,on_delete=models.CASCADE,blank=True,null=True)
    amount = models.FloatField()
    reciept = models.FileField(upload_to="upload")
    expense_date = models.DateField()
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    expenser_name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.property_id.code }"


