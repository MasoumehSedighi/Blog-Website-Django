from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    # author =
    # tag =
    # category =
    # image =
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

