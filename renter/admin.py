from django.contrib import admin

from renter.models import FlatRent, RentCollection, RenterBeneficaries, RepairRecords

# Register your models here.
admin.site.register(RenterBeneficaries)
admin.site.register(FlatRent)
admin.site.register(RepairRecords)
admin.site.register(RentCollection)