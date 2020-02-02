from rest_framework.views import APIView, Response
from .serializers import UserSerializer
from rest_framework import permissions
from core.models import User


class UserDetailView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)



