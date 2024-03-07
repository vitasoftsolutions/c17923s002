from rest_framework import serializers
from loan.serializers import PhoneSerializer
from renter.models import FlatRent, RentCollection, RenterBeneficaries, RepairRecords

class RenterBeneficariesSerializer(serializers.ModelSerializer):
    phone_number = PhoneSerializer(many=True,read_only = True)
    class Meta:
        model = RenterBeneficaries
        fields = '__all__'

class FlatRentSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    property_name = serializers.SerializerMethodField()
    renter_name = serializers.SerializerMethodField()
    class Meta:
        model = FlatRent
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None
    def get_property_name(self, obj):
        # Get the name of the related contractor
        if obj.property_id:
            return obj.property_id.code
        return None
    def get_renter_name(self, obj):
        # Get the name of the related contractor
        if obj.renter_id:
            return obj.renter_id.first_name+ " " +obj.renter_id.last_name
        return None

class FRentCollectionSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    property_name = serializers.SerializerMethodField()
    renter_name = serializers.SerializerMethodField()
    class Meta:
        model = RentCollection
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None
    def get_property_name(self, obj):
        # Get the name of the related contractor
        if obj.property_id:
            return obj.property_id.code
        return None
    def get_renter_name(self, obj):
        # Get the name of the related contractor
        if obj.renter_id:
            return obj.renter_id.first_name+ " " +obj.renter_id.last_name
        return None

class RepairRecordsSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    property_name = serializers.SerializerMethodField()
    renter_name = serializers.SerializerMethodField()
    class Meta:
        model = RepairRecords
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None
    def get_property_name(self, obj):
        # Get the name of the related contractor
        if obj.property_id:
            return obj.property_id.code
        return None
    def get_renter_name(self, obj):
        # Get the name of the related contractor
        if obj.renter_id:
            return obj.renter_id.first_name+ " " +obj.renter_id.last_name
        return None