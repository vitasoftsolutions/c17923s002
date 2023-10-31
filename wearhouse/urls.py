from django.urls import path
from wearhouse import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'material-installment',views.MaterialInstallmentViews,basename="material-installment")
router.register(r'material-purchase',views.MaterialPurchasesViews,basename="material-purchase")
router.register(r'warehouse-items',views.WearhouseItemViews,basename="warehouse-items")
router.register(r'warehouse-dispatch',views.WarehouseMaterialDispatchViews,basename="warehouse-dispatch")
router.register(r'material-payment',views.MaterialPaymentinstallmentViews,basename="material-payment")
urlpatterns = [

]
urlpatterns+= router.urls