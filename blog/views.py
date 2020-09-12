# Create your views here.
from django.utils import timezone
from .models import Post, Tab
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, TabForm


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'devBlog/blog-post.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('home_page')
    else:
        form = PostForm()
    return render(request, 'devBlog/post_edit.html', {'form': form, 'new_post': True})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'devBlog/post_edit.html', {'form': form, 'new_post': False,
                                                      'text': post.text, 'title': post.title})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home_page')


def blog_post(request):
    return render(request, 'devBlog/blog-post.html')


def root_page(request):
    return redirect('home_page')


def home_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'devBlog/home.html', {'posts': posts})


def about(request):
    return render(request, 'devBlog/about.html')


def resume(request):
    tabs = Tab.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'devBlog/resume.html', {'tabs': tabs})


def resume_new(request):
    if request.method == "POST":
        form = TabForm(request.POST)
        if form.is_valid():
            tab = form.save(commit=False)
            tab.author = request.user
            tab.publish()
            return redirect('resume')
    else:
        form = TabForm()
    return render(request, 'devBlog/resume_edit.html', {'form': form, 'new_tab': True})


def resume_edit(request, pk):
    tab = get_object_or_404(Tab, pk=pk)
    if request.method == "POST":
        form = TabForm(request.POST, instance=tab)
        if form.is_valid():
            tab = form.save(commit=False)
            tab.author = request.user
            tab.publish()
            return redirect('resume')
    else:
        form = TabForm(instance=tab)
    return render(request, 'devBlog/resume_edit.html', {'form': form, 'new_tab': False,
                                                        'description': tab.description, 'title': tab.title})
