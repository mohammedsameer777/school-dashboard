from rest_framework import serializers
from .models import Teacher, Student
from django.contrib.auth import authenticate

class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'email', 'name']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'rrn', 'address', 'marks', 'teacher']
        read_only_fields = ['teacher']
