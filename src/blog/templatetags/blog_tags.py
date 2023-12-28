from django import template
from .. import models

register = template.Library()

@register.inclusion_tag('blog/sidebar/latest-posts.html')
def latestposts(arg=3):
    posts = models.Post.objects.filter(status=True).order_by("-published_at")[:arg]
    return {'posts_pup':posts}


@register.inclusion_tag('blog/sidebar/categories.html')
def postcategories():
    cat_dict={}
    categories = models.Category.objects.all()
    for cat in categories:
        cat_dict[cat] = models.Post.objects.filter(status=True, category=cat).count()
    return {'categories':cat_dict}