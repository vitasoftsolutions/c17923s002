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
import os
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import FileUploadParser
from rest_framework import viewsets,parsers
from csvhandler.models import UploadCsv
from csvhandler.serializers import UploadCsvSerializer
from rest_framework import generics
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
    

class UploadCsvCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UploadCsv.objects.all()
    serializer_class = UploadCsvSerializer
    parser_classes = [parsers.MultiPartParser]
    def create(self, request, *args, **kwargs):

        # Implement your custom logic here
        # You can access request.data to get the JSON data
        # You can also access self.serializer_class to work with the serializer

        # Example: Extract and print the JSON data
        json_data = request.data
        

        # You can add your custom logic here
        # For example, you can validate, process, or modify the data before saving

        serializer = self.get_serializer(data=json_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        #print(serializer.data['file'])
        # Split the URL by '/'
        url=serializer.data['file']
        parts = url.split('/')

        # Remove the first three parts and keep the rest
        remaining_parts = parts[3:]

        # Join the remaining parts back together to reconstruct the URL
        result_url = '/'.join(remaining_parts)

        #print(result_url)
        csv_file_path = result_url
        model_name = serializer.data['model_name']
        app_label = serializer.data['app_label']
        model_class = apps.get_model(app_label=app_label, model_name=model_name)
        fields = [field for field in model_class._meta.get_fields() if not field.is_relation]
        field_names = [field.name for field in fields]
        field_names_filtered = [field for field in field_names if field != 'id' and field!='created_at' and field!="is_deleted"]
        print(field_names)
        with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
            csv_reader = csv.reader(file)

            for i, row in enumerate(csv_reader):
                if i == 0:
                    continue
                # Print each row
                user_data = dict(zip(field_names_filtered,row[1:]))
                user = model_class (**user_data)
                user.save()
        print(user_data)
        UploadCsv.objects.all().delete()
        

        # Define the directory path
        directory_path = 'upload/csv'  # Replace with the actual path to your directory

        # Get a list of all files in the directory
        file_list = os.listdir(directory_path)

        # Iterate through the file list and delete each file
        for file_name in file_list:
            file_path = os.path.join(directory_path, file_name)
            
            if os.path.isfile(file_path):
                os.remove(file_path)

        # Optionally, you can print a message to confirm that the files have been deleted
        print(f"All files in '{directory_path}' have been deleted.")

        # csv_file_url =serializer.data['file']
        # response = request.get(csv_file_url)
        # if response.status_code == 200:
        # # Process the CSV content
        #     content = response.text
        #     csv_reader = csv.DictReader(content.splitlines())  # Assuming the CSV has headers

        #     for row in csv_reader:
        #         # Access data for each row using row['column_name']
        #         print(row)
        #         # ... (access other columns as needed)

        #         # Process the data (e.g., save to the
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
