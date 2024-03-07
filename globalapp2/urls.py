from django.urls import path
from globalapp2 import views
from rest_framework.routers import DefaultRouter,SimpleRouter
from .views import MyModelFilterView

router = SimpleRouter()
router.register(r'roles',views.GroupViews,basename="roles")
router.register(r'role-permisson',views.PermissionViews,basename="role-permisson")
router.register(r'app-label',views.AppLabelViews,basename="app-label")
router.register(r'types',views.TypeViews,basename="types")



urlpatterns = [
    path('filter/<str:app_name>/<str:model_name>/', MyModelFilterView.as_view(), name='my-model-filter'),

]
urlpatterns+= router.urls