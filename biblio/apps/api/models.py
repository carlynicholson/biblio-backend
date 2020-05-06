from django.db import models
from ..authentication.models import User


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, blank=True, default='')
    pages = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100, blank=True, default='')
    published = models.IntegerField()
    description = models.TextField()
    is_favorite = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title

