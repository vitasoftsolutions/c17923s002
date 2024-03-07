from django.shortcuts import render

# Create your views here.

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from assets.models import AssetsListing, AssetsSell
from assets.serializers import AssetsListingSerializer, AssetsSellSerializer
from globalapp2.views import BaseViews

from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from django_filters import rest_framework as django_filters
# Create your views here.
class AssetListingViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AssetsListingSerializer
    queryset = AssetsListing
    model_name=AssetsListing
    pagination_class = LimitOffsetPagination
    # filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
class AssetSellViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AssetsSellSerializer
    queryset = AssetsSell
    model_name=AssetsSell
    pagination_class = LimitOffsetPagination
    # filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
