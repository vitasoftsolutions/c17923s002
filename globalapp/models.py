from django.db import models
from datetime import datetime
# Create your models here.
class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.phone_number}"
class IntroInfo(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    phone_number = models.ManyToManyField(PhoneNumber)
    present_address = models.TextField()
    permanent_address = models.TextField(null=True)
    NID_number = models.CharField(max_length=20)
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
    appointment = models.FileField(upload_to="appointment/",null=True,blank=True)
    OPTION_a = 'Active'
    OPTION_b = 'Banned'
    OPTION_c = 'Left'
    CHOICES2 = (
        (OPTION_a, 'Active'),
        (OPTION_b, 'Banned'),
        (OPTION_c, 'Left'),
        
        
    )
    status = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    created_at= models.DateTimeField(blank=True,null=True,default=datetime.now())
class Beneficaries(IntroInfo):
    name=models.CharField(max_length=100,null=True,blank=True)
