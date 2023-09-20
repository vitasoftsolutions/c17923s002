from django.urls import path
from csvhandler import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()


urlpatterns = [
    #path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    #path('upload/', views.CSVUploadView.as_view(), name='csv-upload'),
    path('export-csv/', views.ExportBooksToCSV.as_view(), name='export-csv'),
    path('export-csv/upload/', views.ExportBooksToCSV.as_view(), name='export-csv-upload'),  # New URL for CSV upload
    path('import-csv/', views.ImportBooksFromCSV.as_view(), name='import-csv'),  # New import URL
    path('upload-csv/', views.UploadCsvCreateView.as_view(), name='upload-csv-create'),
]
urlpatterns+= router.urls