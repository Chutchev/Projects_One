from django.urls import include
from django.urls import path
from .views import PostListView,RetrievePostView

urlpatterns = [
     path('post/', PostListView.as_view(), name='post_list'),
     path('post/<int:pk>', RetrievePostView.as_view(), name='post_detail')
]