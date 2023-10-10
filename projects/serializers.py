from rest_framework import serializers

from projects.models import ProjectInfo, UnitModels, propertyModels


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