from django.db import models

from globalapp2.models import CommonModel, Types

# Create your models here.
class ProjectInfo(CommonModel):
    name= models.CharField(max_length=100,blank=True,null=True)
    project_type = models.ForeignKey(Types,on_delete=models.CASCADE,related_name='project_type',blank=True,null=True)
    address = models.TextField()
    area= models.CharField(max_length=20)
    division = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    city_corporation = models.CharField(max_length=20)
    ward_no = models.CharField(max_length=20)
    post_office = models.CharField(max_length=20)
    police_station = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    project_size = models.FloatField()
    project_size_type = models.ForeignKey(Types,on_delete=models.CASCADE,related_name='project_size_type',blank=True,null=True)
    basement_no = models.IntegerField()
    number_of_elevator = models.IntegerField()
    number_of_stairs = models.IntegerField()
    number_of_parking = models.IntegerField()
    number_of_shops = models.IntegerField()
    #join_venture_spliting_ratio = 
    work_start_date = models.DateField()
    expected_handover_date= models.DateField()
    commarcial_floor = models.IntegerField()
    commarcial_unit = models.IntegerField()
    residential_floor = models.IntegerField()
    residential_unit= models.IntegerField()
    def __str__(self):
        return f"{self.name}"
