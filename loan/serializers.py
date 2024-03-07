from rest_framework import serializers
from globalapp2.models import PhoneNumber
from django.contrib.auth import get_user_model
import jwt
from rest_framework.request import Request
from loan.models import LoanBeneficaries, LoanInstallment, LoanLog, LoanTransactions
class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'
class LoanBeneficariesSerializer(serializers.ModelSerializer):
    #jwt_token = serializers.SerializerMethodField()
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = LoanBeneficaries
        fields = '__all__'
    # def get_jwt_token(self, obj):
    # # Generate a JWT token for a user (example)
    #     request: Request = self.context.get('request')
    #     serialized_data = self.serialize_request_data(request)
    #     payload = {
    #     'data': serialized_data,
    #     # Add other claims as needed
    #         }
    #     secret_key = '76485647865478'  # Replace with your actual secret key
    #     token = jwt.encode(payload, secret_key, algorithm='HS256')
    #     return token
class LoanTransactionSerializer(serializers.ModelSerializer):
    giver_name = serializers.SerializerMethodField()
    taker_name = serializers.SerializerMethodField()
    class Meta:
        model = LoanTransactions
        fields = '__all__'
    def get_giver_name(self, obj):
        # Get the name of the related contractor
        if obj.giver_id:
            return obj.giver_id.first_name + " " + obj.giver_id.last_name
        return None
    def get_taker_name(self, obj):
        # Get the name of the related contractor
        if obj.taker_id:
            return obj.taker_id.first_name + " " + obj.taker_id.last_name
        return None
class LoanInstallmenttionSerializer(serializers.ModelSerializer):
    giver_name = serializers.SerializerMethodField()
    taker_name = serializers.SerializerMethodField()
    class Meta:
        model = LoanInstallment
        fields = '__all__'
    def get_giver_name(self, obj):
        # Get the name of the related contractor
        if obj.giver_id:
            return obj.giver_id.first_name + " " + obj.giver_id.last_name
        return None
    def get_taker_name(self, obj):
        # Get the name of the related contractor
        if obj.taker_id:
            return obj.taker_id.first_name + " " + obj.taker_id.last_name
        return None


class LoanLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanLog
        fields = '__all__'


