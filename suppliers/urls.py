from django.urls import path
from suppliers import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'supplier-beneficaries',views.SupplierBeneficariesViews,basename="supplier-beneficaries")
router.register(r'metarials',views.MetarialsViews,basename="metarials")

urlpatterns = [

]
urlpatterns+= router.urls