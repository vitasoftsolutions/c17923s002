import threading
from .models import LoanInstallment, LoanLog,LoanBeneficaries, LoanTransactions, get_current_user

def log_action(giver_id,taker_id,loan_id,author_id,activity):
    
    LoanLog.objects.create(
        giver_id=giver_id,
        author_id = author_id,
        loan_id= loan_id,
        taker_id = taker_id,
        activity = activity
        )


from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from middleware.user_middleware import current_request
##Loan Beneficaries
@receiver(post_save, sender=LoanBeneficaries)
def log_create_update_action(sender, instance, created,user=None,**kwargs):
    activity = "Created" if created else "Updated"
    print(current_request().user)
    #print("working")
    #data = f"{sender.__name__} object: {instance.author_id}"
    user_name = user.email_address if user else "Unknown User"
    #user = my_thread_local.user
    #print(user)
    message = f"{current_request().user} is {activity} {instance.first_name} {instance.last_name} data"
    log_action(author_id=current_request().user,giver_id=None,taker_id=None,loan_id=None, activity=message)

@receiver(pre_delete, sender=LoanBeneficaries)
def log_delete_action(sender, instance, **kwargs):
    activity = "Deleted"
    message = f"{current_request().user} is {activity} in {sender.__name__} table {instance.first_name} {instance.last_name} data"
    log_action(author_id=current_request().user,giver_id=None,taker_id=None,loan_id=None, activity=message)

##Loan Transactions
@receiver(post_save, sender=LoanTransactions)
def log_create_update_action(sender, instance, created,user=None,**kwargs):
    activity = "Created" if created else "Updated"
    print(current_request().user)
    #print("working")
    #data = f"{sender.__name__} object: {instance.author_id}"
    user_name = user.email_address if user else "Unknown User"
    #user = my_thread_local.user
    #print(user)
    message = f"{current_request().user} is {activity} in {sender.__name__} table  {instance.giver_id.first_name} {instance.giver_id.last_name} data"
    log_action(author_id=current_request().user,giver_id=instance.giver_id,taker_id=instance.taker_id,loan_id=None, activity=message)

@receiver(pre_delete, sender=LoanTransactions)
def log_delete_action(sender, instance, **kwargs):
    activity = "Deleted"
    message = f"{current_request().user} is {activity} in {sender.__name__} table  {instance.giver_id.first_name} {instance.giver_id.last_name} data"
    log_action(author_id=current_request().user,giver_id=instance.giver_id,taker_id=instance.taker_id,loan_id=None, activity=message)
##Loan Installment
@receiver(post_save, sender=LoanInstallment)
def log_create_update_action(sender, instance, created,user=None,**kwargs):
    activity = "Created" if created else "Updated"
    print(current_request().user)
    #print("working")
    #data = f"{sender.__name__} object: {instance.author_id}"
    user_name = user.email_address if user else "Unknown User"
    #user = my_thread_local.user
    #print(user)
    message = f"{current_request().user} is {activity} in {sender.__name__} table  {instance.giver_id.first_name} {instance.giver_id.last_name} data"
    log_action(author_id=current_request().user,giver_id=instance.giver_id,taker_id=instance.taker_id,loan_id=None, activity=message)

@receiver(pre_delete, sender=LoanInstallment)
def log_delete_action(sender, instance, **kwargs):
    activity = "Deleted"
    message = f"{current_request().user} is {activity} in {sender.__name__} table  {instance.giver_id.first_name} {instance.giver_id.last_name} data"
    log_action(author_id=current_request().user,giver_id=instance.giver_id,taker_id=instance.taker_id,loan_id=None, activity=message)



