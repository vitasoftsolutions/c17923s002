from rest_framework import serializers
from datetime import datetime
from projects.models import ExpenseByProperty, ProjectInfo, UnitModels, WorkProgress, projectProgress, propertyInstallment, propertyModels, propertyPurchase


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    class Meta:
        model = propertyModels
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitModels
        fields = '__all__'
        depth=1


class projectProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectProgress
        fields = '__all__'


class WorkProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProgress
        fields = '__all__'

class PropertyPurchaseSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    property_code = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    class Meta:
        model = propertyPurchase
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id.exists():
            return [project.name for project in obj.project_id.all()]
        return None
    def get_property_code(self, obj):
        # Get the name of the related contractor
        if obj.property_id.exists():
            return [property.code for property in obj.property_id.all()]
        return None
    def get_customer_name(self, obj):
        # Get the name of the related contractor
        if obj.customer_id:
            return obj.customer_id.first_name + " "+ obj.customer_id.last_name
        return None
   

class PropertyInstallmentSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    property_code = serializers.SerializerMethodField()
    # customer_name = serializers.SerializerMethodField()
    class Meta:
        model = propertyInstallment
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None
    def get_property_code(self, obj):
        # Get the name of the related contractor
        if obj.property_id:
            return obj.property_id.code
        return None
    # def get_customer_name(self, obj):
    #     # Get the name of the related contractor
    #     if obj.customer_id:
    #         return obj.customer_id.first_name + " "+ obj.customer_id.last_name
    #     return None

class ExpensedBypropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseByProperty
        fields = '__all__'