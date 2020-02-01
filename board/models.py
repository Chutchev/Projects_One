from django.db import models
from django.conf import settings


class Tag(models.Model):
    post = models.ManyToManyField('Post')


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
