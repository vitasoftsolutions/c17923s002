from rest_framework import serializers
from contructors.models import AssignContractor, ContractorGarrentor, ContractorPaymnet, ContructorsBeneficaries
from loan.serializers import PhoneSerializer


##test code


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
    contractor_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    class Meta:
        model = AssignContractor
        fields = '__all__'
    def get_contractor_name(self, obj):
        # Get the name of the related contractor
        if obj.contructor_id:
            return obj.contructor_id.first_name
        return None
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None

class ContractorPaymentSerializer(serializers.ModelSerializer):
    contractor_name = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    class Meta:
        model = ContractorPaymnet
        fields = '__all__'
    def get_contractor_name(self, obj):
        # Get the name of the related contractor
        if obj.contructor_id:
            return obj.contructor_id.first_name+ " "+ obj.contructor_id.last_name
        return None
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None