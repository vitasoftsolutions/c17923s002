from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'expenses',views.ExpenseViews,basename="expenses")
router.register(r'incomes',views.IncomeViews,basename="incomes")
urlpatterns = [
   
]
urlpatterns+= router.urls