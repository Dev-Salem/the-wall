from dj_rest_auth.registration.views import RegisterView
from rest_framework import permissions

from .serializers import CustomRegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    permission_classes = [permissions.AllowAny]
