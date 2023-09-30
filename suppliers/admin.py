from django.contrib import admin

from suppliers.models import Metarials, SupplierBeneficaries

# Register your models here.
admin.site.register(SupplierBeneficaries)
admin.site.register(Metarials)