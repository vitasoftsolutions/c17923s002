from django.urls import path
from profileapp import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'business-profile',views.ProfileViews,basename="business-profile")

urlpatterns = [
   
]
urlpatterns+= router.urls