from django.contrib import admin

from contructors.models import ContractorGarrentor, ContructorsBeneficaries

# Register your models here.
admin.site.register(ContructorsBeneficaries)
admin.site.register(ContractorGarrentor)