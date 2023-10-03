from django.contrib import admin
from globalapp2.models import AppLabel, PhoneNumber, Types

from globalapp2.models import Beneficaries



# Register your models here.
admin.site.register(Beneficaries)
admin.site.register(PhoneNumber)
admin.site.register(AppLabel)
admin.site.register(Types)