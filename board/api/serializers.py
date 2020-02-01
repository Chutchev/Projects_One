from rest_framework import serializers
from board.models import Post


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(many=True, slug_field='text', read_only=True)
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
