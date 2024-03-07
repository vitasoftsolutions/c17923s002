from django.contrib import admin

from csvhandler.models import Book,UploadCsv

# Register your models here.
admin.site.register(Book)
admin.site.register(UploadCsv)