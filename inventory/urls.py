from django.urls import path
from inventory import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
#router.register(r'projects',views.ProjectInfoViews,basename="projects")

urlpatterns = [
   
]
urlpatterns+= router.urls