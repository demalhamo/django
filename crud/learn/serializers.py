from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Student



# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     course = serializers.CharField(max_length=100)
#     college = serializers.CharField(max_length=100)
#     address = serializers.CharField(max_length=100)
  
#     def create(self, validated_data):
#         return Student.objects.create(validated_data)
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.course = validated_data.get('course', instance.course)
#         instance.college = validated_data.get('college', instance.college)
#         instance.address = validated_data.get('address', instance.address)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'course', 'college', 'address']


