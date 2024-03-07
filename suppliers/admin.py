from django.contrib import admin

from suppliers.models import Brands, Metarials, SupplierBeneficaries

# Register your models here.
admin.site.register(SupplierBeneficaries)
admin.site.register(Metarials)
admin.site.register(Brands)
