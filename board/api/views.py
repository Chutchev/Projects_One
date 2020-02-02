from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from .serializers import PostSerializer
from board.models import Post
from core.models import User


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if username:
            user = get_object_or_404(User, username=username)
            posts = Post.objects.filter(author=user.id)
            return posts
        return super().get_queryset()


class RetrievePostView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
