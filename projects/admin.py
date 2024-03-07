from django.contrib import admin

from projects.models import ExpenseByProperty, ProjectInfo, UnitModels, WorkProgress, projectProgress, propertyInstallment, propertyModels, propertyPurchase

# Register your models here.
admin.site.register(ProjectInfo)
admin.site.register(WorkProgress)
admin.site.register(projectProgress)
admin.site.register(propertyModels)
admin.site.register(propertyPurchase)
admin.site.register(propertyInstallment)
admin.site.register(ExpenseByProperty)
admin.site.register(UnitModels)