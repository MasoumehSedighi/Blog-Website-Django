from django.contrib import admin
from blog import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'published_at']
    search_fields = ['title', 'content']
    list_filter = ['status']
    empty_value_display = '_empty_'


admin.site.register(models.Category)
admin.site.register(models.Post, PostAdmin)