from rest_framework import serializers

from profileapp.models import BusinessProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'