from rest_framework import serializers
from .models import Student_table

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student_table
        fields=['reg_no','name','email','marks','dob']
