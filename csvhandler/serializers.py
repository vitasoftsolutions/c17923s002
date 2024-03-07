from rest_framework import serializers
from .models import Book,UploadCsv

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UploadCsvSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadCsv
        fields = '__all__'
