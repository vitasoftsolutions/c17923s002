from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.joined_at=datetime.now()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.is_staff = True 
        user.save(using=self._db)
        return user

class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.phone_number}"
class Employee(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=15)
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
    
    CHOICES2 = (
        (OPTION_a, 'Active'),
        (OPTION_b, 'Banned'),
        
        
    )
    
    status = models.CharField(max_length=50, choices=CHOICES2,blank=True,null=True)
    joined_date= models.DateTimeField(blank=True,null=True,default=datetime.now())
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
