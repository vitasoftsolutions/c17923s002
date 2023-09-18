from rest_framework import serializers

from users.models import Employee, PhoneNumber

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['email','password','first_name','last_name']
    def create(self, validated_data):
       user = Employee.objects.create(
       email = validated_data['email'],
       first_name =validated_data['first_name'],
       last_name =validated_data['last_name'],
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
#custom token

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get('email')
        password = attrs.get('password')

        if username_or_email is None or password is None:
            raise ValidationError('Both username/email and password must be provided.')

        user = get_user_model().objects.filter(username=username_or_email).first()
        attrs['email']=user
        if user is None:
            user = get_user_model().objects.filter(email=username_or_email).first()
            attrs['email']=user
        if user is None or not user.check_password(password):
            raise ValidationError('No active account found with the given credentials.')
        
        return super().validate(attrs)