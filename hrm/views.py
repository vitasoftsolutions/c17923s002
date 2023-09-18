from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.models import Beneficaries, PhoneNumber
from globalapp2.views import BaseViews
from hrm.models import Attendance, Leaves, Salaries
from hrm.serializers import AttendenceSerializer, LeavesSerializer, SalariesSerializer
from loan.models import LoanBeneficaries, LoanTransactions
from loan.serializers import LoanBeneficariesSerializer, LoanTransactionSerializer, PhoneSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.views import IsStaff
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from hrm.filters import *
# Create your views here.
class AttendanceViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AttendenceSerializer
    queryset = Attendance
    model_name=Attendance
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = AttendanceFilter # Use the custom filter class

class LeavesViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = LeavesSerializer
    queryset = Leaves
    model_name=Leaves
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = LeavesFilter # Use the custom filter class

class SalaryViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = SalariesSerializer
    queryset = Salaries
    model_name=Salaries
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = SalariesFilter # Use the custom filter class