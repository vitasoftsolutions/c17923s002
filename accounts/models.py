from django.db import models

from globalapp2.models import CommonModel
from users.models import Employee

# Create your models here.
class Expense(CommonModel):
    reason = models.TextField()
    amount = models.FloatField()
    documents = models.FileField()
    expenser_name = models.CharField(max_length=50)
    expense_date = models.DateTimeField()
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.reason}"
class Income(CommonModel):
    reason = models.TextField()
    amount = models.FloatField()
    documents = models.FileField()
    expenser_name = models.CharField(max_length=50)
    expense_date = models.DateTimeField()
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return f"{self.reason}"