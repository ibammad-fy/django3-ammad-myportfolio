from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:4] #we can also write Blog.objects.all() this will load all blog posts however, current query represents recent 4 posts only
    return render(request, 'myBlog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'myBlog/detail.html', {'blog':blog})