from django.urls import path
from owner import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'owner-beneficaries',views.OwnerBeneficariesViews,basename="owner-beneficaries")

urlpatterns = [
   
]
urlpatterns+= router.urls