from django.db import models
from django.conf import settings


class Tag(models.Model):
    text = models.TextField()
    posts = models.ManyToManyField('Post', related_name='tags')


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)
