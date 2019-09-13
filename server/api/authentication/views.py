from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .renderers import UserJSONRenderer
from rest_framework.renderers import JSONRenderer
from .models import User


class RegisterView(APIView):
    """View to register all users to the system
    * Requires no authentication
    * Anyone can register an account
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
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
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)

    def get(self, request, *args, **kwargs):
        pass
