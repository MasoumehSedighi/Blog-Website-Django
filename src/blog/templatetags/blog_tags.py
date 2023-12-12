from django import template
from .. import models

register = template.Library()

@register.inclusion_tag('blog/sidebar/latest-posts.html')
def latestposts(arg=3):
    posts = models.Post.objects.filter(status=True).order_by("-published_at")[:arg]
    return {'posts_pup':posts}