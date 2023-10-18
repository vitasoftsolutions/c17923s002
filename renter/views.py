from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.views import BaseBeneficaries, BaseViews
from renter.models import FlatRent, RentCollection, RenterBeneficaries, RepairRecords
from renter.serializers import FRentCollectionSerializer, FlatRentSerializer, RenterBeneficariesSerializer, RepairRecordsSerializer
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from django_filters import rest_framework as django_filters
# Create your views here.
class RenterBeneficariesViews(BaseBeneficaries):
    serializer_class = RenterBeneficariesSerializer
    queryset = RenterBeneficaries.objects.all()
    #filterset_class = OwnerBenificaiesFilter
    model_name = RenterBeneficaries

class FlatRentViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = FlatRentSerializer
    queryset = FlatRent
    model_name=FlatRent
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]

class RentCollectionViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = FRentCollectionSerializer
    queryset = RentCollection
    model_name=RentCollection
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]

class RepairRecordsViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = RepairRecordsSerializer
    queryset = RepairRecords
    model_name=RepairRecords
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]