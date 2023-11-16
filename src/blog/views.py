from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def blog_home_view(request):
    posts = models.Post.objects.filter(status=True)
    context={
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(models.Post, pk=pid)
    context = {
        'post': post
    }
    return render(request, 'blog/blog-single.html', context)