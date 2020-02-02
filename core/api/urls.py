from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, re_path
from .views import UserDetailView

urlpatterns = [
    path('me/', UserDetailView.as_view(), name='user')
]