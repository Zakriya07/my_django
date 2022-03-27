from .models import *
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Student

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Parent
