from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import Employee

# Create your models here.
class Attendance(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee',blank=True,null=True)
    author = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='author',blank=True,null=True)
    status = models.BooleanField(blank=True,null=True,default=False)
    date = models.DateTimeField(blank=True,null=True,default=datetime.now())
    work_hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.employee_id}"
    
class Leaves(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_leaves',default=None)
    author = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='author_leaves',default=None)
    from_date= models.DateField()
    to_date = models.DateField()
    days = models.IntegerField(null=True,blank=True)
    leave_type= models.CharField(max_length=100)
    reason = models.TextField()
    status = models.BooleanField(blank=True,null=True,default=False)
    apply_date = models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.from_date and self.to_date:
            print(self.to_date - self.from_date)
            self.days=(self.to_date - self.from_date).days
        else:
            self.days=0
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.employee_id}"
    
class Salaries(models.Model):
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_salary',default=None)
    author = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='author_salary',default=None)
    salary = models.IntegerField()
    days = models.IntegerField(null=True,blank=True)
    loan = models.IntegerField(null=True,blank=True)
    due = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(blank=True,null=True,default=False)
    date = models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.employee_id}"