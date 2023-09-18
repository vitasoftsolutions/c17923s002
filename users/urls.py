from django.urls import path
from users import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'employee',views.AllEmployeeView,basename="employee")
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.RegisterUser.as_view()),
    path('profile/',views.EmployeeView.as_view()),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
urlpatterns+= router.urls
