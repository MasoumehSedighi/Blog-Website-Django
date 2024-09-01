from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home', views.blog_home_view, name='blog-home'),
    path('<int:pid>', views.blog_single_view, name='blog-single'),
    path('category/<str:cat_name>', views.blog_home_view, name='blog-category'),
    path('author/<str:author_username>', views.blog_home_view, name='blog-author'),
    path('search/',views.blog_search_view,name='search'),

]
