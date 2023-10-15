from rest_framework import serializers
from contructors.models import AssignContractor, ContractorGarrentor, ContractorPaymnet, ContructorsBeneficaries
from loan.serializers import PhoneSerializer


class ContructorsBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = ContructorsBeneficaries
        fields = '__all__'
class ContructorsGarrentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorGarrentor
        fields = '__all__'

class AssignContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignContractor
        fields = '__all__'

class ContractorPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorPaymnet
        fields = '__all__'