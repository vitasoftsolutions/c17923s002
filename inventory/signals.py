from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from inventory.models import MaterialDispatch, ProductInventories
from projects.models import ProjectInfo
from wearhouse.models import WarehouseMaterialDispatch, WearhouseItem

@receiver(post_save, sender=MaterialDispatch)
def inventory_material_dispatch(sender, instance, created, **kwargs):
    product_object = ProductInventories.objects.get(id=instance.inventory_item_id.id)
    print(instance.check_status)
    if instance.check_status=="Check out":
        product_object.use_quantity = product_object.use_quantity+instance.quantity
    elif instance.check_status=="Check in":
        product_object.use_quantity = product_object.use_quantity-instance.quantity
    else:
        product_object.quantity = product_object.quantity-instance.quantity
    product_object.save()
    if created:
        if instance.check_status=="Return" or instance.check_status=="Swap":
            warehouse_id = WearhouseItem.objects.create(
                inventory_id = ProductInventories.objects.get(id=instance.inventory_item_id.id),
                quantity = instance.quantity,
                due_quantity = 0
            )
            if instance.check_status=="Swap":
                ProductInventories.objects.create(
                        purchase_for = ProjectInfo.objects.get(id=instance.project_id.id),
                        amount = 0,
                        amount_due = 0,
                        amount_advance = 0,
                        quantity = instance.quantity,
                        #materials = material_ids,
                        recieved_quantity = instance.quantity,
                )

