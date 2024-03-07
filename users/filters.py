
from rest_framework import filters
from django_filters import rest_framework as django_filters
from users.models import Employee
from django.utils import timezone
class EmployeeFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    email = django_filters.CharFilter(lookup_expr='icontains')
    username = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    nid_number = django_filters.CharFilter(lookup_expr='icontains')
    joined_date = django_filters.DateFilter(
        field_name='joined_date',
        lookup_expr='date__exact',
        #widget=django_filters.widgets.DateInput(attrs={'type': 'date'}),
        #label='Created At (YYYY-MM-DD)',
    )
    class Meta:
        model = Employee
        fields = ['email','username','first_name','last_name','nid_number','joined_date']  # Add more fields if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the 'created_at' filter
        self.filters['joined_date'].extra['initial'] = timezone.datetime(2023, 8, 11, 18, 3, 8)