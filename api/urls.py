from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileView, StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='students')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]


