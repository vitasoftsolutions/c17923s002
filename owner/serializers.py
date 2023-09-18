from rest_framework import serializers
from owner.models import OwnerBeneficaries
from loan.serializers import PhoneSerializer


class OwnerBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = OwnerBeneficaries
        fields = '__all__'