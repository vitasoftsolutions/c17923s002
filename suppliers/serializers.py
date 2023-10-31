
from rest_framework import serializers
from globalapp2.models import PhoneNumber
from loan.serializers import PhoneSerializer


from suppliers.models import Brands, SupplierBeneficaries,Metarials


class SupliersBeneficariesSerializer(serializers.ModelSerializer):
    #jwt_token = serializers.SerializerMethodField()
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = SupplierBeneficaries
        fields = '__all__'
class MetarialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metarials
        fields = '__all__'

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'