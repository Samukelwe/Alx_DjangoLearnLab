
from django.contrib.auth.models import User
from django.db import models
from .models import Post


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # Import 'Post' model as a string
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

from .post import Post  # Import 'Post' model locally

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)

    # Your existing fields and methods