from django.db import models
from django.urls import reverse

class Reytings(models.Model):
    name = models.CharField(max_length=200)
    subscribers = models.IntegerField()
    views = models.IntegerField()
    vaqt = models.IntegerField()
    link = models.TextField()
    def __str__(self):
        return self.name

class BlogPosts(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs')



























