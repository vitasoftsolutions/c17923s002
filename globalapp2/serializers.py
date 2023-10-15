from django.contrib.auth.models import Group,Permission
from rest_framework import serializers

from globalapp2.models import AppLabels, Typess

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        #depth=2
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class AppLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppLabels
        fields = '__all__'

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typess
        fields = '__all__'