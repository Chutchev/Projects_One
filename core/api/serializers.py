from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'last_login',
                  'first_name',
                  'last_name',
                  'bio',
                  'location',
                  'birth_date',
                  'groups',)
