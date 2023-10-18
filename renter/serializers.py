from rest_framework import serializers
from loan.serializers import PhoneSerializer
from renter.models import FlatRent, RentCollection, RenterBeneficaries, RepairRecords

class RenterBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = RenterBeneficaries
        fields = '__all__'

class FlatRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlatRent
        fields = '__all__'

class FRentCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentCollection
        fields = '__all__'

class RepairRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRecords
        fields = '__all__'