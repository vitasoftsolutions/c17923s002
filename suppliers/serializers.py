
from rest_framework import serializers
from globalapp2.models import PhoneNumber
from loan.serializers import PhoneSerializer


from suppliers.models import SupplierBeneficaries


class SupliersBeneficariesSerializer(serializers.ModelSerializer):
    #jwt_token = serializers.SerializerMethodField()
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = SupplierBeneficaries
        fields = '__all__'