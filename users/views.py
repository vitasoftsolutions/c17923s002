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

 #############custom permission class#########
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
  
class AllEmployeeView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsStaff]
    serializer_class = AllUserSerializer
    queryset = Employee.objects.all()
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



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
