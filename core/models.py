from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    # pk aka id --> numbers
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
