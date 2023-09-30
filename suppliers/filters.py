
from rest_framework import filters
from django_filters import rest_framework as django_filters
from globalapp2.models import PhoneNumber
from django.utils import timezone

from suppliers.models import Metarials, SupplierBeneficaries

class SupplierBenfcaiesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    giver_name = django_filters.CharFilter(lookup_expr='icontains')
    nid_number = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='date__exact',
        #widget=django_filters.widgets.DateInput(attrs={'type': 'date'}),
        #label='Created At (YYYY-MM-DD)',
    )
    class Meta:
        model = SupplierBeneficaries
        fields = ['first_name','last_name','email','giver_name','nid_number']  # Add more fields if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the 'created_at' filter
        self.filters['created_at'].extra['initial'] = timezone.datetime(2023, 8, 11, 18, 3, 8)
class MetarialsFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Metarials
        fields = ['name']  # Add more fields if needed