from django.urls import path
from inventory import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'material-dispatch',views.MaterialDispatchsViews,basename="material-dispatch")
router.register(r'product-inventories',views.ProductInventoriesViews,basename="material-purchase")
urlpatterns = [
   
]
urlpatterns+= router.urls