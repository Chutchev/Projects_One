from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework import permissions
from .serializers import PostSerializer
from board.models import Post


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class RetrievePostView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        post = self.get_object()
        print(post)
        print(args)
        print(kwargs)
        return super().update(request, *args, **kwargs)
