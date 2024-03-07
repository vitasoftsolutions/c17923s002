from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from inventory.models import ProductInventories
from projects.models import ProjectInfo
from suppliers.models import SupplierBeneficaries
from wearhouse.models import MaterialInstallment, MaterialPurchases, WarehouseMaterialDispatch, WearhouseItem
from django.db.models.signals import m2m_changed
from functools import partial
material_data = None
@receiver(post_save, sender=MaterialPurchases)
def material_purchase_effect(sender, instance, created, **kwargs):
    
    print("begin data: ",instance.materials.all())
    post_save.disconnect(material_purchase_effect, sender=MaterialPurchases)
    instance.due_quantity = instance.quantity - instance.recieved_quantity
    instance.save()
    print(instance.materials.all())
    # if instance.purchase_for:
    #     ProductInventories.objects.create(
    #             purchase_for = '',
    #             vendor_id = '',
    #             sr_name = instance.sr_name,
    #             sr_number = instance.sr_number,
    #             purchase_code = in
    #             amount = 
    #             amount_due = 
    #             amount_advance = 
    #             quantity = 
    #             recieved_quantity = 
    #             due_quantity = 
    #     )
    post_save.connect(material_purchase_effect, sender=MaterialPurchases)
    if created:
        # m2m_changed.connect(handle_m2m_change, sender=MaterialPurchases.materials.through)
        # instance.save()
        # # m2m_changed.connect(handle_m2m_change, sender=MaterialPurchases.materials.through)
        # # material_ids = handle_m2m_change(sender=MaterialPurchases.materials.through, instance=instance, action="post_add")
        # # m2m_changed.disconnect(handle_m2m_change, sender=MaterialPurchases.materials.through)

        # post_save.connect(material_purchase_effect, sender=MaterialPurchases)
        # global material_data
        # print("data: ",material_data)
        # material_ids = [material.id for material in instance.materials.all()]
        # print(material_ids)
        instance.save()
        
        productpurchase = MaterialPurchases.objects.get(id=instance.id)
        # print("product: ",productpurchase.materials)
        post_save.disconnect(material_purchase_effect, sender=MaterialPurchases)
        instance.amount_due = instance.amount-instance.amount_advance
        if instance.recieved_quantity:
            instance.due_quantity = instance.quantity-instance.recieved_quantity
        instance.save()
        post_save.connect(material_purchase_effect, sender=MaterialPurchases)
        if instance.purchase_for:
            if instance.vendor_id:
                vendor = SupplierBeneficaries.objects.get(id=instance.vendor_id.id)
            else:
                vendor=None
            try:
                pri = ProductInventories.objects.create(
                        purchase_for = ProjectInfo.objects.get(id=instance.purchase_for.id),
                        vendor_id = vendor,
                        sr_name = instance.sr_name,
                        sr_number = instance.sr_number,
                        amount = instance.amount,
                        amount_due = instance.amount_due,
                        amount_advance = instance.amount_advance,
                        quantity = instance.quantity,
                        #materials = material_ids,
                        recieved_quantity = instance.recieved_quantity,
                        due_quantity = instance.due_quantity
                )
            except:
                pri=None
            #pri.materials.set(material_ids)
            #pri.save()
            
        if pri:
            pri_id = ProductInventories.objects.get(id=pri.id)
        else:
            pri_id=None

        WearhouseItem.objects.create(
            purchase_id = MaterialPurchases.objects.get(id=instance.id),
            inventory_id = pri_id,
            quantity = instance.recieved_quantity

        )
        partial_handle_m2m_change = partial(handle_m2m_change, prid=pri.id)
        m2m_changed.connect(partial_handle_m2m_change, sender=MaterialPurchases.materials.through)
        instance.save()
        
        m2m_changed.connect(partial_handle_m2m_change, sender=MaterialPurchases.materials.through)
######### Material installment########
@receiver(post_save, sender=MaterialInstallment)
def material_installment(sender, instance, created, **kwargs):
    objects = MaterialPurchases.objects.get(purchase_code=instance.purchase_id)
    objects.due_quantity = objects.due_quantity-instance.quantity
    objects.recieved_quantity = objects.recieved_quantity+instance.quantity
    objects.save()
    warehouse = WearhouseItem.objects.get(purchase_id=instance.purchase_id)
    warehouse.quantity = warehouse.quantity+instance.quantity
    warehouse.save()
######### Warehouse Save ########
@receiver(post_save, sender=WearhouseItem)
def warehouse_save(sender, instance, created, **kwargs):
    
    if instance.inventory_id:

        objects = ProductInventories.objects.get(id=instance.inventory_id.id)
        post_save.disconnect(warehouse_save, sender=WearhouseItem)
        WarehouseMaterialDispatch.objects.create(
            warehouse_item_id=WearhouseItem.objects.get(id=instance.id),
            quantity = instance.quantity-objects.recieved_quantity,
            check_status="Check out"
        )
        post_save.connect(warehouse_save, sender=WearhouseItem)
        objects.recieved_quantity= instance.quantity
        objects.due_quantity= objects.quantity-instance.quantity
        objects.save()
        post_save.disconnect(warehouse_save, sender=WearhouseItem)
        instance.due_quantity = 0
        #instance.save()
        post_save.connect(warehouse_save, sender=WearhouseItem)
        
       
        
        

    
######### Material Dispatch ########
@receiver(post_save, sender=WarehouseMaterialDispatch)
def wearhouse_dispaatch(sender, instance, created, **kwargs):
    pass




###helper function
def handle_m2m_change(prid,sender, instance, action, **kwargs):
    if action == "post_add":
        # print("function data: ",instance.materials.all())
        # print("pri id : ",prid)
        pri = ProductInventories.objects.get(id=prid)
        material_ids = [material.id for material in instance.materials.all()]
        pri.materials.set(material_ids)
        m2m_changed.disconnect(handle_m2m_change, sender=MaterialPurchases.materials.through)



        