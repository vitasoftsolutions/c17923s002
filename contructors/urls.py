from django.urls import path
from contructors import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'contructor-beneficaries',views.ContructorBeneficariesViews,basename="contructor-beneficaries")
router.register(r'contructor-guarantor',views.ContractorGarrentorViews,basename="contructor-guarantor")
router.register(r'assigned-contractor',views.AssignContractorViews,basename="assigned-contractor")
router.register(r'contractor-payment',views.ContractorPaymentViews,basename="contractor-payment")
urlpatterns = [
   
]
urlpatterns+= router.urls