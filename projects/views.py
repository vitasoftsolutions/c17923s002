from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.ed import encode_jwt
from globalapp2.views import BaseViews
from projects.models import ExpenseByProperty, ProjectInfo, UnitModels, WorkProgress, projectProgress, propertyInstallment, propertyModels, propertyPurchase
from projects.serializers import ExpensedBypropertySerializer, ProjectSerializer, PropertyInstallmentSerializer, PropertyPurchaseSerializer, PropertySerializer, UnitSerializer, WorkProgressSerializer, projectProgressSerializer
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from django_filters import rest_framework as django_filters
from datetime import datetime
from django.utils import timezone
from dateutil import parser

def identify_time_format(time_string):
    try:
        parsed_time = parser.parse(time_string)
        return parsed_time
    except ValueError as e:
        return f"Error: {e}"






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
    filterset_fields = ['project_id', 'type', 'code']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(queryset, many=True)
        #paginate_data=self.get_paginated_response(serializer.data)
        if 'limit' in request.query_params and 'offset' in request.query_params:
    #         # Apply pagination based on provided parameters
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                token = encode_jwt({"data": serializer.data})
                return self.get_paginated_response({"token": token})
                
        token = encode_jwt({"data": serializer.data})
        return Response({"token": token})
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     # Check if pagination parameters are provided in the request
    #     if 'limit' in request.query_params and 'offset' in request.query_params:
    #         # Apply pagination based on provided parameters
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.serializer_class(page, many=True)
    #             return self.get_paginated_response(serializer.data)
    #     else:
    #         # Apply default pagination if no parameters are provided
    #         page = self.paginate_queryset(queryset)
    #         if page is not None:
    #             serializer = self.serializer_class(page, many=True)
    #             token = encode_jwt({"data": serializer.data})
    #             return Response({"token": token})

    #     # If no pagination is applied, serialize the entire queryset
    #     serializer = self.serializer_class(queryset, many=True)
    #     token = encode_jwt({"data": serializer.data})
    #     return Response({"token": token})
    #filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
    # def list(self, request, *args, **kwargs):
    #     project_id = self.request.query_params.get('project_id')
    #     project_type = self.request.query_params.get('project_type')
    #     flat_code = self.request.query_params.get('flat_code')
    #     if project_id and project_type and flat_code:
    #         print(project_id,project_type)
    #         queryset = propertyModels.objects.filter(project_id=project_id,type=project_type,code=flat_code)
    #         print(queryset)
    #     else:
    #         # Return all the data from the queryset
    #         queryset = self.get_queryset()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # def list(self, request, *args, **kwargs):
    #     project_id = self.request.query_params.get('project_id')
    #     project_type = self.request.query_params.get('project_type')
    #     flat_code = self.request.query_params.get('flat_code')

    #     queryset = self.queryset

    #     if project_id is not None:
    #         queryset = queryset.filter(project_id=project_id)
    #     if project_type is not None:
    #         queryset = queryset.filter(type=project_type)
    #     if flat_code is not None:
    #         queryset = queryset.filter(code=flat_code)

    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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

class PropertyPurchaseFilterViews(BaseViews):
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



