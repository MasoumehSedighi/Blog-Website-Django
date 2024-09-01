from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category for blog posts.

    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post.
    """

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # tag =
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/', default='blog/default.png')
    counted_views = models.PositiveIntegerField(default=0)
    content = models.TextField()
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        ordering = ['created_at']


    def __str__(self):
        return self.title

    @classmethod
    def get_next_post(cls, current_id):
        """
        Retrieves the next published blog post based on the current post ID.
        """
        try:
            return cls.objects.filter(status=True, id__gt=(current_id)).order_by("id")[0]
        except:
            return None


    @classmethod
    def get_previous_post(cls, current_id):
        """
        Retrieves the previous published blog post based on the current post ID.
        """
        try:
            return cls.objects.filter(status=True, id__lt=(current_id)).order_by("-id")[0]
        except:
            return None
