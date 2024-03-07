from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions
from globalapp2.models import PhoneNumber
from globalapp2.views import BaseViews
from profileapp.models import BusinessProfile
from profileapp.serializers import ProfileSerializer
from users.views import IsStaff,IsAdmin
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class ProfileViews(BaseViews):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = ProfileSerializer
    queryset = BusinessProfile
    model_name= BusinessProfile
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    #filterset_class = LoanInstallmentFilter # Use the custom filter class
    def perform_create(self, serializer):
        instance = serializer.save()
        return instance  # Returning the instance after saving
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        new_data = {key: value for key, value in serializer.initial_data.items() if key != "phone_number"}
        data=new_data
        #print(data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        id=self.perform_create(serializer)
        
        
        message=""
        data = []
        for i in range(len(serializer.initial_data)):
            if f'phone_number[{i}][name]' in serializer.initial_data:
               p_id= PhoneNumber.objects.create(
                first_name= serializer.initial_data[f'phone_number[{i}][name]'],
                last_name = '',
                relation= serializer.initial_data[f'phone_number[{i}][relation]'],
                phone_number= serializer.initial_data[f'phone_number[{i}][number]'],
                status= True,
                role= "",

                 )
               data.append(p_id.id)
               print(p_id.id)
        print(data)
        id.phone_number.set(data)
        

       
        
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message":f"Business profile Created. {message}",
            "data":serializer.data,

        }, status=status.HTTP_201_CREATED, headers=headers)
        #return Response({"message": "data check done"})