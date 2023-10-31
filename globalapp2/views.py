
from globalapp2.ed import encode_jwt
from django.shortcuts import render
from rest_framework import viewsets,parsers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from globalapp2.models import AppLabels, Beneficaries, PhoneNumber, Typess
from globalapp2.serializers import AppLabelSerializer, GroupSerializer, PermissionSerializer, TypesSerializer
from django.contrib.auth.models import Group,Permission
from loan.models import LoanBeneficaries, LoanInstallment, LoanLog, LoanTransactions
from loan.serializers import LoanBeneficariesSerializer, LoanInstallmenttionSerializer, LoanLogSerializer, LoanTransactionSerializer, PhoneSerializer
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from users.views import IsStaff,IsAdmin
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from loan.filters import *
import json
from django.http import QueryDict
# Create your views here.
class BaseViews(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model_name.objects.filter(is_deleted=False)
    # def list(self, request, *args, **kwargs):
    #     # Custom logic for the list (GET) method
    #     data = self.get_queryset()
    #     serializer = self.get_serializer(data, many=True)
    #     # print(serializer.data)
    #     # token = encode_jwt({"data":serializer.data})
    #     # return Response({"token": token})
    #     return self.get_paginated_response(serializer.data)
    def list(self, request, *args, **kwargs):
        # Get the paginated queryset
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            # Serialize the paginated data
            serializer = self.get_serializer(page, many=True)

            # Return the paginated response
            token = encode_jwt({"data":serializer.data})
            return self.get_paginated_response({"token":token})

        # If there is no pagination, serialize the entire queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data without pagination
        token = encode_jwt({"data":serializer.data})
        return Response({"token":token})
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Data deleted. But you can recover your data"})
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        item = self.get_object()
        item.status = not item.status
        item.save()
        return Response({"message": "Status changed"})
    

class BaseBeneficaries(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = None
    queryset = None
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = None  # Use the custom filter class
    parser_classes = [parsers.MultiPartParser]
    def list(self, request, *args, **kwargs):
        # Get the paginated queryset
        try:
            ordering = self.request.query_params.get('order')
            print(ordering)
        except:
            pass
        try:
            phone = self.request.query_params.get('phone')
            ben_ids_queryset = PhoneNumber.objects.filter(phone_number=phone)
            ben_id_list = []
            for ben_id_obj in ben_ids_queryset:
                ben_id_list.append(ben_id_obj.ben_id)
            print(ben_id_list)
            unique_beneficiaries_set = set()

            # Create a new list to store the unique objects in order
            unique_beneficiaries_list = []

            # Iterate through the original list
            for beneficiary in ben_id_list:
                # Check if the object is not in the set (i.e., it's unique)
                if beneficiary not in unique_beneficiaries_set:
                    # Add the unique object to the set and the new list
                    unique_beneficiaries_set.add(str(beneficiary))
                    unique_beneficiaries_list.append(str(beneficiary))
            print(list(unique_beneficiaries_set))
            unique_beneficiaries_set=list(unique_beneficiaries_set)
        except:
            pass
        queryset = self.filter_queryset(self.get_queryset())
        if ordering == "asc":
            queryset = queryset.order_by('first_name')
        elif ordering == "dsc":
            queryset = queryset.order_by('-first_name')
        if  unique_beneficiaries_set:

            queryset=self.model_name.objects.filter(first_name=unique_beneficiaries_set[0])

        page = self.paginate_queryset(queryset)

        if page is not None:
            # Serialize the paginated data
            serializer = self.get_serializer(page, many=True)

            # Return the paginated response
            token = encode_jwt({"data":serializer.data})
            return self.get_paginated_response({"token":token})

        # If there is no pagination, serialize the entire queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data without pagination
        token = encode_jwt({"data":serializer.data})
        return Response({"token":token})
    def perform_create(self, serializer):
        instance = serializer.save()
        return instance  # Returning the instance after saving
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        test_data = self.get_serializer(data=request.data)
        #phone_numbers = serializer.initial_data.getlist('phone_number')
        #json_data = json.dumps(serializer.initial_data)
        #print(json_data)
        # querydict_data = QueryDict(serializer.initial_data)
        # data_dict = {}
        # for key, value in querydict_data.items():
        #     data_dict[key] = value
        # #json_data = json.dumps(data_dict)
        # print(querydict_data)
        try:
            phone_numbers = serializer.initial_data['phone_number']
            test_numbers="got number"
        except:
            phone_numbers = []
            test_numbers="number not found"
        new_data = {key: value for key, value in serializer.initial_data.items() if key != "phone_number"}
        data=new_data
        #print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        id=self.perform_create(serializer)
        id=int(id.id)
        
        message=""
        print(phone_numbers)
       
        for phone_number in phone_numbers:
            #print(phone_number)
            #print(type(phone_number['role']))
            PhoneNumber.objects.create(
                name= phone_number['name'],
                relation= phone_number['relation'],
                phone_number= phone_number['phone_number'],
                status= True,
                role= "",
                ben_id= Beneficaries.objects.get(id=id)

            )
            #message="Phone number also created"

        
            #message="Phone number not created"
        #remove from here
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message":f"Beneficaries Created. {message}",
            "data":serializer.data,

        }, status=status.HTTP_201_CREATED, headers=headers)
        #return Response({"message": "data check done"})



class GroupViews(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsAdmin]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViews(mixins.ListModelMixin,viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsAdmin]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = None



class AppLabelViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AppLabelSerializer
    queryset = AppLabels
    model_name=AppLabels
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class

class TypeViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = TypesSerializer
    queryset = Typess
    model_name=Typess
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
    def get_queryset(self):
        label_name = self.request.query_params.get('label_name')
        #print(self.model_name.objects.filter(is_deleted=False,project_id__id=id))
        return self.model_name.objects.filter(is_deleted=False,app_label__name=label_name)



    



