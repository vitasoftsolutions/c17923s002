from rest_framework import filters
from django_filters import rest_framework as django_filters
from contructors.models import ContractorGarrentor, ContructorsBeneficaries

from customers.models import CustomerBeneficaries



class ContructorBenificaiesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    giver_name = django_filters.CharFilter(lookup_expr='icontains')
    NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ContructorsBeneficaries
        fields = ['first_name','last_name','email','giver_name','NID_number']  # Add more fields if needed

class ContructorGarrentorFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = ContractorGarrentor
        fields = ['first_name','last_name','email','NID_number']  # Add more fields if needed