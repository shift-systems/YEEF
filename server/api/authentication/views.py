from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import User, Profile
from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerialiser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .renderers import UserJSONRenderer, ProfileJSONRenderer
from rest_framework.renderers import JSONRenderer
from .models import User


class RegisterView(APIView):
    """View to register all users to the system
    * Requires no authentication
    * Anyone can register an account
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request, *args, **kwargs):
        user = request.data.get('user')

        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    """View to login a given user
    * Requires no authentication
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request, *args, **kwargs):
        user = request.data.get('user')
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileView(APIView):
    """View to handle profiles
    * Requires no authentication
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerialiser
    renderer_classes = (ProfileJSONRenderer,)

    def get(self, request, *args, **kwargs):
        """Get a profile for a logged in user"""
        user = request.user
        if user.is_authenticated:
            profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """Update profile for a logged in user"""
        profile = request.data.get('profile')
        user = profile.pop('user', None)
        serializer = self.serializer_class(
            data=profile,  partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.update(user, serializer.validated_data)
        serialized_data = self.serializer_class(data)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
