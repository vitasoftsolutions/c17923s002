from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from globalapp2.models import Beneficaries, PhoneNumber
from users.models import Employee
import threading



def get_current_user():
    """
    Get the current user from the request's thread.
    """
    return getattr(threading.local(), 'user', "Hello")
# Create your models here.
class LoanBeneficaries(Beneficaries):
    pass
class LoanTransactions(models.Model):
    giver_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='given_loans')
    taker_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='taken_loans')
    amount = models.FloatField(validators=[MinValueValidator(1)])
    OPTION_a = 'Fixed'
    OPTION_b = 'Percentage'
    CHOICES = (
        (OPTION_a, 'Fixed'),
        (OPTION_b, 'Percentage'),
    )
    
    return_type = models.CharField(max_length=50, choices=CHOICES,blank=True,null=True)
    interest = models.FloatField()
    instalment = models.IntegerField(validators=[MinValueValidator(1)])
    interested_amount = models.FloatField(blank=True,null=True)
    return_amount = models.FloatField(blank=True,null=True)
    current_amount = models.FloatField(blank=True,null=True)
    status = models.BooleanField(default=True)
    last_payed  = models.DateField(blank=True,null=True)
    created_at = models.DateField(default=timezone.now().date(),null=True,blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def save(self, *args, **kwargs):
        if self.return_type == 'Percentage':
            self.interested_amount = (self.amount*self.interest)/100
            self.return_amount=self.amount+self.interested_amount
        else:
            self.return_amount = self.amount+self.interest
        is_first_time = not self.pk
        if is_first_time:
            self.current_amount=self.return_amount
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.giver_id}"

class LoanInstallment(models.Model):
    giver_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='given_installment')
    taker_id = models.ForeignKey(LoanBeneficaries,on_delete=models.CASCADE,related_name='taken_installment')
    author_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    amount = models.FloatField(validators=[MinValueValidator(1)])
    instalment = models.IntegerField(validators=[MinValueValidator(1)])
    document = models.FileField(upload_to='documents')
    loan_id = models.ForeignKey(LoanTransactions,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now().date(),null=True,blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.giver_id}"
    
class LoanLog(models.Model):
    giver_id = models.ForeignKey(LoanBeneficaries,on_delete=models.SET_NULL,related_name='given_activity',blank=True,null=True)
    taker_id = models.ForeignKey(LoanBeneficaries,on_delete=models.SET_NULL,related_name='taken_activity',blank=True,null=True)
    author_id = models.ForeignKey(Employee,on_delete=models.SET_NULL,blank=True,null=True)
    loan_id = models.ForeignKey(LoanTransactions,on_delete=models.SET_NULL,blank=True,null=True)
    activity= models.TextField(blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    is_deleted = models.BooleanField(default=False,null=True,blank=True)
    def __str__(self):
        return f"{self.activity}"