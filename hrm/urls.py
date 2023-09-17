from django.urls import path
from hrm import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'attendance',views.AttendanceViews,basename="attendance")
router.register(r'leaves',views.LeavesViews,basename="leaves")
router.register(r'salaries',views.SalaryViews,basename="salaries")


urlpatterns = [

]
urlpatterns+= router.urls
