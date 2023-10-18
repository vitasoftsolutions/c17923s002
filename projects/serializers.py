from rest_framework import serializers

from projects.models import ExpenseByProperty, ProjectInfo, UnitModels, WorkProgress, projectProgress, propertyInstallment, propertyModels, propertyPurchase


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = propertyModels
        fields = '__all__'


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
    class Meta:
        model = propertyPurchase
        fields = '__all__'

class PropertyInstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = propertyInstallment
        fields = '__all__'

class ExpensedBypropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseByProperty
        fields = '__all__'