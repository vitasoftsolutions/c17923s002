from django.shortcuts import render

from globalapp2.views import BaseViews
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from inventory.models import ProductInventories
from inventory.serializers import MaterialDispatchSerializer
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters import rest_framework as django_filters
from rest_framework import filters
from wearhouse.serializers import MaterialInstallmentsSerializer, MaterialPurchasesSerializer, WarehouseMaterialDispatchSerializer, WearhouseItemSerializer
# Create your views here.
class MaterialDispatchsViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MaterialDispatchSerializer
    queryset = ProductInventories
    model_name=ProductInventories
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class

class ProductInventoriesViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MaterialDispatchSerializer
    queryset = ProductInventories
    model_name=ProductInventories
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class