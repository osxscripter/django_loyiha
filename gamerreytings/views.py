from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Reytings, BlogPosts

class StrimerReyting(ListView):
    model = Reytings
    template_name = 'home.html'
class BlogPost(ListView):
    model = BlogPosts
    template_name = 'generic.html'
class AddPost(CreateView):
    model = BlogPosts
    template_name = 'newPost.html'
    fields = ['title', 'author', 'body']
