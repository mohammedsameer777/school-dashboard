from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Teacher, Student
from .serializers import StudentSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
        if not email or not name or not password:
            return Response({'error': 'Missing fields'}, status=400)
        if Teacher.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=400)
        Teacher.objects.create_user(email=email, name=name, password=password)
        return Response({'message': 'Teacher registered successfully'})

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Student.objects.filter(teacher=self.request.user)
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ProfileView(APIView):
    def get(self, request):
        user=request.user
        return Response({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
