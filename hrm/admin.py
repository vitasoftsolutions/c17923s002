from django.contrib import admin

from hrm.models import Attendance, Leaves, Salaries

# Register your models here.
admin.site.register(Attendance)
admin.site.register(Leaves)
admin.site.register(Salaries)