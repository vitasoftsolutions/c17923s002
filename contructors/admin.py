from django.contrib import admin

from contructors.models import AssignContractor, ContractorGarrentor, ContractorPaymnet, ContructorsBeneficaries

# Register your models here.
admin.site.register(ContructorsBeneficaries)
admin.site.register(ContractorGarrentor)
admin.site.register(AssignContractor)
admin.site.register(ContractorPaymnet)