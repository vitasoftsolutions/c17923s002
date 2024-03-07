from django.contrib import admin

from loan.models import LoanBeneficaries, LoanInstallment, LoanLog, LoanTransactions

# Register your models here.
admin.site.register(LoanBeneficaries)
admin.site.register(LoanTransactions)
admin.site.register(LoanInstallment)
admin.site.register(LoanLog)