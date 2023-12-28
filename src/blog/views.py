from django.shortcuts import render, get_object_or_404
from . import models
# Create your views here.

def blog_home_view(request, cat_name=None):
    posts = models.Post.objects.filter(status=True)
    if cat_name:
            posts = posts.filter(category__name=cat_name)
    context={
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    post = get_object_or_404(models.Post, pk=pid, status=True)
    next_post = models.Post.get_next_post(current_id=pid)
    previous_post = models.Post.get_previous_post(current_id=pid)
    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post
    }
    return render(request, 'blog/blog-single.html', context)