from rest_framework import generics
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
class BasicView(generics.views.APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})

    def post(self, request):
        return Response({"message": "Hello, World!"})

class CreateUserView(generics.CreateAPIView):
    model = CustomUser
    serializer_class = CustomUserSerializer
    