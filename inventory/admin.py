from django.contrib import admin

from inventory.models import MaterialDispatch, ProductInventories

# Register your models here.
admin.site.register(MaterialDispatch)
admin.site.register(ProductInventories)