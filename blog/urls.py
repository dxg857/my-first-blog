from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('home', views.home_page, name='home_page'),
    path('about', views.about),
    path('blog-post', views.blog_post),
    path('blog-list', views.blog_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
]