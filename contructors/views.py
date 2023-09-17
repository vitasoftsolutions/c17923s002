from django.shortcuts import render
from contructors.models import ContractorGarrentor, ContructorsBeneficaries
from contructors.serializers import ContructorsBeneficariesSerializer, ContructorsGarrentorSerializer
from customers.models import CustomerBeneficaries
from customers.serializers import CustomerBeneficariesSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from globalapp2.ed import encode_jwt
from globalapp2.models import Beneficaries, PhoneNumber
from globalapp2.views import BaseViews
from users.views import IsStaff
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from contructors.filters import *
# Create your views here.
class ContructorBeneficariesViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = ContructorsBeneficariesSerializer
    queryset = ContructorsBeneficaries
    model_name=ContructorsBeneficaries
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = ContructorBenificaiesFilter # Use the custom filter class
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        phone_numbers = serializer.initial_data['phone_number']
        
        for phone_number in phone_numbers:
            print(phone_number)
            print(type(phone_number['role']))
            PhoneNumber.objects.create(
                name= phone_number['name'],
                relation= phone_number['relation'],
                phone_number= phone_number['phone_number'],
                status= True,
                role= Beneficaries.objects.get(id=phone_number['role']),
                ben_id= Beneficaries.objects.get(id=phone_number['ben_id'])

            )
        new_data = {key: value for key, value in serializer.initial_data.items() if key != "phone_number"}
        data=new_data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ContractorGarrentorViews(BaseViews):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = ContructorsGarrentorSerializer
    queryset = ContractorGarrentor
    model_name=ContractorGarrentor
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = ContructorGarrentorFilter # Use the custom filter class