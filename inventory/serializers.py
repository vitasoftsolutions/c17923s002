from rest_framework import serializers

from inventory.models import MaterialDispatch, ProductInventories



class MaterialDispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialDispatch
        fields = '__all__'


class ProductInventoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventories
        fields = '__all__'

