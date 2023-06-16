from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegistrationSerializer, LoginSerializer, RegisterUpdateSerializer

from drf_yasg.utils import swagger_auto_schema


class RegistrationAPIView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = CustomUser.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        refresh = RefreshToken.for_user(user)

        return Response({
            'status': 'success',
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })


class RegisterUpdateView(generics.GenericAPIView):
    serializer_class = RegisterUpdateSerializer

    @swagger_auto_schema(request_body=RegisterUpdateSerializer,
                         responses={200: 'User updated successfully', 400: 'Bad Request'})
    def put(self, request):
        user = request.user

        serializer = RegisterUpdateSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

