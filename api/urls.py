from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, StudentViewSet, ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('', include(router.urls)),
]

