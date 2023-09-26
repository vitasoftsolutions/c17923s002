from django.urls import path
from globalapp2 import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'roles',views.GroupViews,basename="roles")
router.register(r'role-permisson',views.PermissionViews,basename="role-permisson")



urlpatterns = [

]
urlpatterns+= router.urls