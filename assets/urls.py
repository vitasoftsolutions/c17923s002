from django.urls import path
from assets import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
# router.register(r'owner-beneficaries',views.OwnerBeneficariesViews,basename="owner-beneficaries")
router.register(r'assets-sell',views.AssetSellViews,basename="assets-sell")
router.register(r'assets',views.AssetListingViews,basename="assets")
urlpatterns = [
   
]
urlpatterns+= router.urls