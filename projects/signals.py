from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from globalapp2.helper import number_to_alphabetic_order

from projects.models import ProjectInfo, UnitModels, propertyModels


@receiver(post_save, sender=ProjectInfo)
def unit_flat_create(sender, instance, created, **kwargs):
    print(instance.commarcial_floor+instance.residential_floor)
    if created:
        floor =instance.commarcial_floor+instance.residential_floor
        for i in range(1,floor+1):
            if i<=instance.commarcial_floor:
                print("coomarcial floor")
                unit = UnitModels.objects.create(
                    project_id = ProjectInfo.objects.get(id=instance.id),
                    unit_floor = i,
                    type= "Commarcial"

                )
                print(unit)
                
            else:
                print("coomarcial floor")
                unit=UnitModels.objects.create(
                    project_id = ProjectInfo.objects.get(id=instance.id),
                    unit_floor = i,
                    type= "Ressidential"

                )
                related_object_ids = []
                for j in range(1,instance.residential_unit+1):
                    #print(f"{number_to_alphabetic_order(i)+str(j)}")
                    property=propertyModels.objects.create(
                        code= number_to_alphabetic_order(i)+str(j),
                        project_id = ProjectInfo.objects.get(id=instance.id),
                        size = (instance.project_size/instance.residential_unit)

                    )
                    #print(property.id)
                    related_object_ids.append(property.id)
                related_objects = propertyModels.objects.filter(id__in=related_object_ids)
                unit.unit_property.add(*related_objects)
                unit.save()
    else:
         print("not working")