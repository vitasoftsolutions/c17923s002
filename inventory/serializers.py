from rest_framework import serializers

from inventory.models import MaterialDispatch, ProductInventories



class MaterialDispatchSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    class Meta:
        model = MaterialDispatch
        fields = '__all__'
    def get_project_name(self, obj):
        # Get the name of the related contractor
        if obj.project_id:
            return obj.project_id.name
        return None


class ProductInventoriesSerializer(serializers.ModelSerializer):
    inventory_name = serializers.SerializerMethodField()
    class Meta:
        model = ProductInventories
        fields = '__all__'
    def get_inventory_name(self, obj):
        # Get the name of the related contractor
        if obj.purchase_for:
            return obj.purchase_for.name
        return None

