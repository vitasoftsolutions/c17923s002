from django.shortcuts import render

from globalapp2.views import BaseViews
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from django_filters import rest_framework as django_filters
from rest_framework import filters
from wearhouse.models import MaterialInstallment, MaterialPaymentinstallment, MaterialPurchases, WarehouseMaterialDispatch, WearhouseItem

from wearhouse.serializers import MaterialInstallmentsSerializer, MaterialPaymentinstallmentSerializer, MaterialPurchasesSerializer, WarehouseMaterialDispatchSerializer, WearhouseItemSerializer
# Create your views here.
class MaterialPurchasesViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MaterialPurchasesSerializer
    queryset = MaterialPurchases
    model_name=MaterialPurchases
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class


class WearhouseItemViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = WearhouseItemSerializer
    queryset = WearhouseItem
    model_name=WearhouseItem
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class


class MaterialInstallmentViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MaterialInstallmentsSerializer
    queryset = MaterialInstallment
    model_name=MaterialInstallment
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class


class WarehouseMaterialDispatchViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = WarehouseMaterialDispatchSerializer
    queryset = WarehouseMaterialDispatch
    model_name=WarehouseMaterialDispatch
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class

class MaterialPaymentinstallmentViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = MaterialPaymentinstallmentSerializer
    queryset = MaterialPaymentinstallment
    model_name=MaterialPaymentinstallment
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = MetarialsFilter # Use the custom filter class