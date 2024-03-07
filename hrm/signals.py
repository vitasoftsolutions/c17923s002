from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from hrm.models import Attendance

@receiver(post_save, sender=Attendance)
def inventory_material_dispatch(sender, instance, created, **kwargs):
    print("Hrm Signals working")

