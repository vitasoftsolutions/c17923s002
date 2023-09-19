# from django.http import HttpResponse
# from django.shortcuts import render
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import permissions
# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework import viewsets
# # Create your views here.
# import csv
# from rest_framework import generics, status
# from rest_framework.parsers import FileUploadParser
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from users.views import IsStaff
# from .models import Book
# from .serializers import BookSerializer
# from django.apps import apps

# class BookListCreateView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class CSVUploadView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     parser_classes = (FileUploadParser,)

#     def post(self, request, *args, **kwargs):
#         file_serializer = BookSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @authentication_classes([JWTAuthentication])
# @permission_classes([permissions.IsAuthenticated, IsStaff])
# def export_books_to_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     model_name = request.GET.get('model', 'default_value1')
#     app_label = request.GET.get('app_label', 'default_value1')
#     print(model_name)
#     model_class = apps.get_model(app_label=app_label, model_name=model_name)
#     response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

#     writer = csv.writer(response)
    

#     books = model_class.objects.all()
#     #fields = model_class._meta.get_fields()
#     fields = [field for field in model_class._meta.get_fields() if field.is_relation == False]
#     field_names = [field.name for field in fields]
#     writer.writerow(field_names)
#     print(field_names)
#     for book in books:
#         value= []
#         for field in field_names:
#             field=getattr(book, field)
#             value.append(field)
#         print(value)    
#         writer.writerow(value)

#     return response
# class CsvHandler(viewsets.ModelViewSet):
#     @action(detail=True, methods=['post'])
#     def export_books_to_csv(request):
#         response = HttpResponse(content_type='text/csv')
#         model_name = request.GET.get('model', 'default_value1')
#         app_label = request.GET.get('app_label', 'default_value1')
#         print(model_name)
#         model_class = apps.get_model(app_label=app_label, model_name=model_name)
#         response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

#         writer = csv.writer(response)
        

#         books = model_class.objects.all()
#         #fields = model_class._meta.get_fields()
#         fields = [field for field in model_class._meta.get_fields() if field.is_relation == False]
#         field_names = [field.name for field in fields]
#         writer.writerow(field_names)
#         print(field_names)
#         for book in books:
#             value= []
#             for field in field_names:
#                 field=getattr(book, field)
#                 value.append(field)
#             print(value)    
#             writer.writerow(value)

#         return response



from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.apps import apps
import csv
import io
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import FileUploadParser
class ExportBooksToCSV(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        model_name = request.GET.get('model', 'default_value1')
        app_label = request.GET.get('app_label', 'default_value1')
        model_class = apps.get_model(app_label=app_label, model_name=model_name)
        response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'

        writer = csv.writer(response)

        books = model_class.objects.all()
        fields = [field for field in model_class._meta.get_fields() if not field.is_relation]
        field_names = [field.name for field in fields]
        writer.writerow(field_names)

        for book in books:
            value = []
            for field in field_names:
                attribute_value = getattr(book, field)
                value.append(attribute_value)
            writer.writerow(value)

        return response

class ImportBooksFromCSV(APIView):
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]
    parser_classes = (FileUploadParser,)

    def post(self, request):
        # Check if a CSV file was uploaded
        csv_file = request.data.get('csv_file')
        if not csv_file:
            return JsonResponse({'error': 'No CSV file uploaded'}, status=400)

        try:
            # Assuming the CSV file has a header row with field names
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_data = list(csv.reader(decoded_file))
        except Exception as e:
            return JsonResponse({'error': 'Invalid CSV file'}, status=400)

        # Process and manipulate the CSV data as needed
        # For example, you can parse it, update the database, etc.
        # Here, we simply return the CSV data as a JSON response
        return JsonResponse({'csv_data': csv_data})