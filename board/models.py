from django.db import models
from django.conf import settings


class Tag(models.Model):
    text = models.TextField()
    posts = models.ManyToManyField('Post', related_name='tags', blank=True)

    def __str__(self):
        return self.text


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'Post: {self.content[:51]}'


