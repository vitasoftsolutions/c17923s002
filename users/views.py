from django.shortcuts import render
from globalapp2.models import PhoneNumber


from users.models import Employee
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from users.serializers import AllUserSerializer, CustomTokenObtainPairSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from globalapp2.ed import encode_jwt
from rest_framework import filters
from django_filters import rest_framework as django_filters
from users.filters import EmployeeFilter
#from globalapp2.views import BaseBeneficaries
############################################# PERMISSION ############################################
class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_staff)
    

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin)

# Create your views here.
class RegisterUser(APIView):
    def post(self,requests):
        serializer = UserSerializer(data = requests.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({
            'status':403,
            "errors": serializer.errors,
            "message": "User data not valid"
            
            })
        serializer.save()
        user = Employee.objects.get(email= serializer.data['email'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'status':200,
            "payload": serializer.data,
            'refresh': str(refresh),
            'access': str(refresh),
            "message": "You logged in successfully"
            
            })
class EmployeeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AllUserSerializer

    def get(self, request, format=None):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        print(user_id)
        user = Employee.objects.filter(id=user_id)
        serializer = AllUserSerializer(user, many=True)
        return Response(serializer.data)
    # def post(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk=None):
    #     token = self.request.headers.get('Authorization').split()[1]
    #     payload = AccessToken(token).payload
    #     user_id = payload.get('user_id')
    #     user = Employee.objects.get(id=user_id)
    #     serializer = self.serializer_class(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk=None):
    #     token = self.request.headers.get('Authorization').split()[1]
    #     payload = AccessToken(token).payload
    #     user_id = payload.get('user_id')
    #     user = Employee.objects.get(id=user_id)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    def patch(self, request, pk=None):
        token = self.request.headers.get('Authorization').split()[1]
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        user = Employee.objects.get(id=user_id)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class AllEmployeeView(BaseBeneficaries):
#     serializer_class = AllUserSerializer
#     queryset = Employee.objects.all()
#     #filterset_class = CustomerBenificaiesFilter
#     model_name = Employee
  ############################################################### All Employee Previous code ##############################################
class AllEmployeeView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AllUserSerializer
    pagination_class = LimitOffsetPagination
    queryset = Employee.objects.all()
    filter_backends = [filters.OrderingFilter, django_filters.DjangoFilterBackend]
    filterset_class = EmployeeFilter  # Use the custom filter class
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     #phone number create code:
    #     phone_numbers = serializer.initial_data['phone_number']
    #     phone_ids=[]
    #     for phone_number in phone_numbers:
    #         try:
    #             phone_id = PhoneNumber.objects.get(phone_number=phone_number)
    #             phone_ids.append(phone_id.pk)
    #         except:
    #             phone_id = PhoneNumber.objects.create(
    #                 phone_number=phone_number
    #             )
    #             phone_ids.append(phone_id.pk)
        
    #     serializer.initial_data['phone_number']=phone_ids
    #     data=serializer.initial_data
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
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

            queryset=Employee.objects.filter(first_name=unique_beneficiaries_set[0])

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
        print(serializer.initial_data)
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
                role= Employee.objects.get(id=id),
                ben_id= Employee.objects.get(id=id)

            )
            #message="Phone number also created"

        
            #message="Phone number not created"
        #remove from here
        headers = self.get_success_headers(serializer.data)
        return Response({
            "message":f"Employee Created. {message}",
            "data":serializer.data,

        }, status=status.HTTP_201_CREATED, headers=headers)
        #return Response({"message": "data check done"})



# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

    
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        print(response.data['access'])
        token=response.data['access']
        # if response.status_code == status.HTTP_200_OK:
        #     user = self.user  # Assuming you have a 'user' attribute in your custom authentication logic
        #     if user and user.is_authenticated:
        #         # Customize the response to include user data
        #         user_data = {
        #             "id": user.id,
        #             "email": user.email,
        #             "username": user.username,
        #             # Add more fields as needed
        #         }
        #         response.data["user"] = user_data
        payload = AccessToken(token).payload
        user_id = payload.get('user_id')
        print(user_id)
        user = Employee.objects.filter(id=user_id)
        serializer = AllUserSerializer(user, many=True)
        print(serializer.data)
        response.data["user"] = encode_jwt({"data":serializer.data})
        return response


