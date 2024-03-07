from rest_framework import serializers

from wearhouse.models import MaterialInstallment, MaterialPaymentinstallment, MaterialPurchases, WarehouseMaterialDispatch, WearhouseItem

class MaterialPurchasesSerializer(serializers.ModelSerializer):
    purchase_for_name = serializers.SerializerMethodField()
    vendor_name = serializers.SerializerMethodField()
    class Meta:
        model = MaterialPurchases
        fields = '__all__'
    def get_purchase_for_name(self, obj):
        # Get the name of the related contractor
        if obj.purchase_for:
            return obj.purchase_for.name
        return None
    def get_vendor_name(self, obj):
        # Get the name of the related contractor
        if obj.vendor_id:
            return obj.vendor_id.first_name+ " " +obj.vendor_id.last_name
        return None


class WearhouseItemSerializer(serializers.ModelSerializer):
    purchase_code = serializers.SerializerMethodField()
    inventory_name = serializers.SerializerMethodField()
    class Meta:
        model = WearhouseItem
        fields = '__all__'
    def get_purchase_code(self, obj):
        # Get the name of the related contractor
        if obj.purchase_id:
            return obj.purchase_id.purchase_code
        return None
    def get_inventory_name(self, obj):
        # Get the name of the related contractor
        if obj.inventory_id:
            return obj.inventory_id.purchase_for.name
        return None
        


class MaterialInstallmentsSerializer(serializers.ModelSerializer):
    purchase_code = serializers.SerializerMethodField()
    class Meta:
        model = MaterialInstallment
        fields = '__all__'
    def get_purchase_code(self, obj):
        # Get the name of the related contractor
        if obj.purchase_id:
            return obj.purchase_id.purchase_code
        return None
    


class WarehouseMaterialDispatchSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = WarehouseMaterialDispatch
        fields = '__all__'

class MaterialPaymentinstallmentSerializer(serializers.ModelSerializer):
    purchase_code = serializers.SerializerMethodField()
    class Meta:
        model = MaterialPaymentinstallment
        fields = '__all__'
    def get_purchase_code(self, obj):
        # Get the name of the related contractor
        if obj.purchase_id:
            return obj.purchase_id.purchase_code
        return None




