from django.urls import path
from . import views


urlpatterns = [
    path('home', views.blog_home_view),
    path('single', views.blog_single_view)
    
]
