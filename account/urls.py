from django.urls import path
from .views import RegistrationAPIView, LoginView, RegisterUpdateView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', RegisterUpdateView.as_view(), name='profile'),
]

