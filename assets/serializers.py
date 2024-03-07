from rest_framework import serializers

from assets.models import AssetsListing, AssetsSell


class AssetsListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsListing
        fields = '__all__'

class AssetsSellSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsSell
        fields = '__all__'