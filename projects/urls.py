from django.urls import path
from projects import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'projects',views.ProjectInfoViews,basename="projects")
router.register(r'property',views.PropertyViews,basename="property")
router.register(r'floor',views.UnitViews,basename="floor")
urlpatterns = [
   
]
urlpatterns+= router.urls