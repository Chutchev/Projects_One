from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, re_path
from .views import PostListView,RetrievePostView

urlpatterns = [
    # TODO: Вынести авторизацию в core модуль
    path('auth/', obtain_auth_token, name='auth'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', RetrievePostView.as_view(), name='post_detail'),
]