from django.contrib import admin

from wearhouse.models import MaterialInstallment, MaterialPaymentinstallment, MaterialPurchases, WarehouseMaterialDispatch, WearhouseItem

# Register your models here.
admin.site.register(MaterialPurchases)
admin.site.register(MaterialInstallment)
admin.site.register(WearhouseItem)
admin.site.register(WarehouseMaterialDispatch)
admin.site.register(MaterialPaymentinstallment)