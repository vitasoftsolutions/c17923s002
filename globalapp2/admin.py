from django.contrib import admin
from globalapp2.models import AppLabels, PhoneNumber, Typess

from globalapp2.models import Beneficaries



# Register your models here.
admin.site.register(Beneficaries)
admin.site.register(PhoneNumber)
admin.site.register(AppLabels)
admin.site.register(Typess)