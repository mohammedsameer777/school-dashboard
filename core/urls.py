from django.urls import path, include
from .views import RegisterView, TeacherProfileView, StudentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', TeacherProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
