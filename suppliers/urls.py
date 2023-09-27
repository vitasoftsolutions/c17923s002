from django.urls import path
from suppliers import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'supplier-beneficaries',views.SupplierBeneficariesViews,basename="supplier-beneficaries")


urlpatterns = [

]
urlpatterns+= router.urls
