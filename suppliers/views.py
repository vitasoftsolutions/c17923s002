from django.shortcuts import render
from globalapp2.views import BaseBeneficaries,BaseViews
from suppliers.filters import MetarialsFilter, SupplierBenfcaiesFilter
from suppliers.models import Metarials, SupplierBeneficaries
from rest_framework_simplejwt.authentication import JWTAuthentication
from suppliers.serializers import MetarialsSerializer, SupliersBeneficariesSerializer
from rest_framework import permissions
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters import rest_framework as django_filters
from rest_framework import filters
# Create your views here.
class SupplierBeneficariesViews(BaseBeneficaries):
    serializer_class = SupliersBeneficariesSerializer
    queryset = SupplierBeneficaries.objects.all()
    filterset_class = SupplierBenfcaiesFilter
    model_name = SupplierBeneficaries

class MetarialsViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MetarialsSerializer
    queryset = Metarials
    model_name=Metarials
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = MetarialsFilter # Use the custom filter class