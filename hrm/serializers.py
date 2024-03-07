from rest_framework import serializers

from hrm.models import Attendance, Leaves, Salaries



class AttendenceSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    class Meta:
        model = Attendance
        fields = '__all__'
    def get_employee_name(self, obj):
        # Get the name of the related contractor
        if obj.employee_id:
            return obj.employee_id.first_name + " " + obj.employee_id.last_name
            # return obj.employee_id.first_name + " " + obj.employee_id.last_name
        return None

class LeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaves
        fields = '__all__'
        

class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = '__all__'
