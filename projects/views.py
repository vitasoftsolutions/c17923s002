from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.views import BaseViews
from projects.models import ExpenseByProperty, ProjectInfo, UnitModels, WorkProgress, projectProgress, propertyInstallment, propertyModels, propertyPurchase
from projects.serializers import ExpensedBypropertySerializer, ProjectSerializer, PropertyInstallmentSerializer, PropertyPurchaseSerializer, PropertySerializer, UnitSerializer, WorkProgressSerializer, projectProgressSerializer
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from django_filters import rest_framework as django_filters
# Create your views here.
class ProjectInfoViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = ProjectSerializer
    queryset = ProjectInfo
    model_name=ProjectInfo
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class


class PropertyViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = PropertySerializer
    queryset = propertyModels
    model_name=propertyModels
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class

class UnitViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = UnitSerializer
    queryset = UnitModels
    model_name=UnitModels
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    def get_queryset(self):
        id = self.request.query_params.get('id')
        #print(self.model_name.objects.filter(is_deleted=False,project_id__id=id))
        return self.model_name.objects.filter(is_deleted=False,project_id__id=id)
    

class WorkProgressViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = WorkProgressSerializer
    queryset = WorkProgress
    model_name=WorkProgress
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class

class ProjectprogressViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = projectProgressSerializer
    queryset = projectProgress
    model_name=projectProgress
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class

class PropertyPurchaseViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = PropertyPurchaseSerializer
    queryset = propertyPurchase
    model_name=propertyPurchase
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
class PropertyInstallmentViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = PropertyInstallmentSerializer
    queryset = propertyInstallment
    model_name=propertyInstallment
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
class ExpensedbyPropertyViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = ExpensedBypropertySerializer
    queryset = ExpenseByProperty
    model_name=ExpenseByProperty
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class



