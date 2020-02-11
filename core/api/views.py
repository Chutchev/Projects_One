from rest_framework.views import Response, APIView
from .serializers import UserSerializer
from rest_framework import permissions, status
from core.models import User


class UserDetailView(APIView):
    permission_classes = (permissions.BasePermission,)

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(self.request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = UserSerializer(self.request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
