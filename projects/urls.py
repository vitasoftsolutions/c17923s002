from django.urls import path
from projects import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
#router.register(r'customers-beneficaries',views.CustomerBeneficariesViews,basename="customers-beneficaries")

urlpatterns = [
   
]
urlpatterns+= router.urls