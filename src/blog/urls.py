from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home', views.blog_home_view, name='blog-home'),
    path('<int:pid>', views.blog_single_view, name='blog-single')
    
]
