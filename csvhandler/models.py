from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
class UploadCsv(models.Model):
    model_name = models.CharField(max_length=50)
    app_label= models.CharField(max_length=50,null=True,blank=True)
    file =models.FileField(upload_to="csv",validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    def __str__(self):
        return self.name