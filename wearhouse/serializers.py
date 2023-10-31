from rest_framework import serializers

from wearhouse.models import MaterialInstallment, MaterialPaymentinstallment, MaterialPurchases, WarehouseMaterialDispatch, WearhouseItem

class MaterialPurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialPurchases
        fields = '__all__'


class WearhouseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WearhouseItem
        fields = '__all__'


class MaterialInstallmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialInstallment
        fields = '__all__'


class WarehouseMaterialDispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseMaterialDispatch
        fields = '__all__'

class MaterialPaymentinstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialPaymentinstallment
        fields = '__all__'




