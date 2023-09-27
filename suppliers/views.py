from django.shortcuts import render
from globalapp2.views import BaseBeneficaries
from suppliers.filters import SupplierBenfcaiesFilter
from suppliers.models import SupplierBeneficaries

from suppliers.serializers import SupliersBeneficariesSerializer

# Create your views here.
class SupplierBeneficariesViews(BaseBeneficaries):
    serializer_class = SupliersBeneficariesSerializer
    queryset = SupplierBeneficaries.objects.all()
    filterset_class = SupplierBenfcaiesFilter
    model_name = SupplierBeneficaries