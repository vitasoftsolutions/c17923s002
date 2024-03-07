from rest_framework import serializers
from customers.models import CustomerBeneficaries
from loan.serializers import PhoneSerializer


class CustomerBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = CustomerBeneficaries
        fields = '__all__'