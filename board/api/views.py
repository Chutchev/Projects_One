from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import PostSerializer
from board.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
