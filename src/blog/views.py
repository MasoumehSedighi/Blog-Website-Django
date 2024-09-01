from django.shortcuts import render, get_object_or_404
from . import models


def blog_home_view(request, cat_name=None, author_username=None):
    """
    displaying the blog home page with a list of posts.
    filtering posts based on the optional category name and author username.
    """

    posts = models.Post.objects.filter(status=True)
    if cat_name:
            posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    context={
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    """
    displaying a single blog post based on the post ID.
    retrieving the next and previous published posts for navigation.
    """

    post = get_object_or_404(models.Post, pk=pid, status=True)
    next_post = models.Post.get_next_post(current_id=pid)
    previous_post = models.Post.get_previous_post(current_id=pid)
    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post
    }
    return render(request, 'blog/blog-single.html', context)
