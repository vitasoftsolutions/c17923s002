
from rest_framework import filters
from django_filters import rest_framework as django_filters

from hrm.models import Attendance, Leaves, Salaries

class AttendanceFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    employee_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    author__first_name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.BooleanFilter(lookup_expr='exact')
    date = django_filters.DateFilter(lookup_expr='exact')
    class Meta:
        model = Attendance
        fields = ['employee_id__first_name','author__first_name','status','date']  # Add more fields if needed

class LeavesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    employee_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    author__first_name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.BooleanFilter(lookup_expr='exact')
    from_date = django_filters.DateFilter(lookup_expr='exact')
    to_date = django_filters.DateFilter(lookup_expr='exact')
    class Meta:
        model = Leaves
        fields = ['employee_id__first_name','author__first_name','status','from_date','to_date']  # Add more fields if needed

class SalariesFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    employee_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    author__first_name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.BooleanFilter(lookup_expr='exact')
    date = django_filters.DateFilter(lookup_expr='exact')
    salary = django_filters.CharFilter(lookup_expr='exact')
    class Meta:
        model = Salaries
        fields = ['employee_id__first_name','author__first_name','status','date','salary']  # Add more fields if needed