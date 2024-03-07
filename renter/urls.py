from django.urls import path
from renter import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'renter-beneficaries',views.RenterBeneficariesViews,basename="renter-beneficaries")
router.register(r'flate-rent',views.FlatRentViews,basename="flate-rent")
router.register(r'rent-collection',views.RentCollectionViews,basename="rent-collection")
router.register(r'repair-records',views.RepairRecordsViews,basename="repair-records")


urlpatterns = [
   
]
urlpatterns+= router.urls