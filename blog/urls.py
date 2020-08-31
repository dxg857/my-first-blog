from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_page),
    path('home', views.home_page, name='home_page'),
    path('about', views.about),
    path('resume', views.resume, name='resume'),
    path('resume/<int:pk>/edit', views.resume_edit, name='resume_edit'),
    path('resume/new/', views.resume_new, name='resume_new'),
    path('blog-post', views.blog_post),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post_delete'),
]
