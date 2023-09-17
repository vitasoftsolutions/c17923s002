from rest_framework import filters
from django_filters import rest_framework as django_filters

from owner.models import OwnerBeneficaries



class OwnerBenificaiesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    giver_name = django_filters.CharFilter(lookup_expr='icontains')
    NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = OwnerBeneficaries
        fields = ['first_name','last_name','email','giver_name','NID_number']  # Add more fields if needed