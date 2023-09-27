
from rest_framework import filters
from django_filters import rest_framework as django_filters
from globalapp2.models import PhoneNumber
from django.utils import timezone
from loan.models import LoanBeneficaries, LoanInstallment, LoanLog, LoanTransactions

class LoanBenfcaiesFilter(django_filters.FilterSet):
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
        model = LoanBeneficaries
        fields = ['first_name','last_name','email','giver_name','nid_number']  # Add more fields if needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the initial value for the 'created_at' filter
        self.filters['created_at'].extra['initial'] = timezone.datetime(2023, 8, 11, 18, 3, 8)


class LoanTransactionsFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    giver_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__email = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__email = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanTransactions
        fields = ['giver_id__first_name','giver_id__last_name','giver_id__email','giver_id__NID_number','taker_id__first_name','taker_id__last_name','taker_id__email','taker_id__NID_number']  # Add more fields if needed

        #Phone Filter
class PhoneFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    role__first_name = django_filters.CharFilter(lookup_expr='icontains')
    role__last_name = django_filters.CharFilter(lookup_expr='icontains')
    ben_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    ben_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    phone_number =django_filters.CharFilter(lookup_expr='icontains')
    name= django_filters.CharFilter(lookup_expr='icontains')
    relation = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PhoneNumber
        fields = ['role__first_name','role__last_name','ben_id__first_name','ben_id__last_name','phone_number','name','relation']  # Add more fields if needed


        #Loan Installment Filter
class LoanInstallmentFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    giver_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__email = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__email = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanInstallment
        fields = ['giver_id__first_name','giver_id__last_name','giver_id__email','giver_id__NID_number','taker_id__first_name','taker_id__last_name','taker_id__email','taker_id__NID_number'] 


class LoanLogFilter(django_filters.FilterSet):
    # Define filters based on the fields you want to allow searching on
    giver_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__email = django_filters.CharFilter(lookup_expr='icontains')
    giver_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__first_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__last_name = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__email = django_filters.CharFilter(lookup_expr='icontains')
    taker_id__NID_number = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = LoanLog
        fields = ['giver_id__first_name','giver_id__last_name','giver_id__email','giver_id__NID_number','taker_id__first_name','taker_id__last_name','taker_id__email','taker_id__NID_number']