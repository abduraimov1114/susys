from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render

from .models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context)   

def example(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'example.html', context)