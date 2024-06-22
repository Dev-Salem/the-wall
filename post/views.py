from rest_framework.generics import views
from rest_framework.response import Response


class BasicView(views.APIView):
    def get(self, request):
        return Response("Hello from Basic")
