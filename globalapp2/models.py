from django.db import models
from datetime import datetime
from django.utils.module_loading import import_string
from django.core.validators import RegexValidator

from users.models import Employee


#from loan.models import LoanBeneficaries
# Create your models here.
class Common(models.Model):
    status = models.BooleanField(default=True,null=True,blank=True)
    created_at= models.DateTimeField(default=datetime.now(),blank=True,null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    
    
class IntroInfo(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    author_id=models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    present_address = models.TextField()
    permanent_address = models.TextField(null=True)
    nid_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\d+$',  # Regular expression to match digits only
                message='Only digits are allowed.',
                code='invalid_digit'
            ),        ]
        )
    nid_front = models.FileField(
        upload_to="nid/",
        verbose_name='NID Image (Front)',
        null=True,
        blank=True
        )
    nid_back = models.FileField(
        upload_to="nid/",
        verbose_name='NID Image (Back)',
        null=True,
        blank=True
        )
    profile_picture = models.ImageField(upload_to="profile/",null=True,blank=True)
    
    
    status = models.BooleanField(default=True,null=True,blank=True)
    created_at= models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.first_name}"
class Beneficaries(IntroInfo):
    pass

class PhoneNumber(models.Model):
    #Beneficiaries = import_string('globalapp2.models.Beneficiaries')
    role = models.ForeignKey(Beneficaries,on_delete=models.CASCADE,related_name='role',blank=True,null=True)
    ben_id = models.ForeignKey(Beneficaries,on_delete=models.CASCADE,related_name='benid',blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    relation= models.CharField(max_length=100,blank=True,null=True)
    phone_number = models.CharField(max_length=15)
    status = models.BooleanField(default=True,null=True,blank=True)
    created_at= models.DateTimeField(default=datetime.now(),blank=True,null=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.phone_number}"
