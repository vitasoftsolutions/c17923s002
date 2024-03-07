from django.urls import path
from loan import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'loan-beneficaries',views.AllLoanBeneficaries,basename="loan-beneficaries")
router.register(r'loan-transactions',views.AllLoanTransactions,basename="loan-transactions")
router.register(r'phone',views.PhoneViews,basename="phone")
router.register(r'loan-installment',views.LoanInstallmentViews,basename="loan-installment")
router.register(r'loan-log',views.LoanLogViewSet,basename="loan-log")

urlpatterns = [

]
urlpatterns+= router.urls
