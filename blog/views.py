from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    last = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').reverse()[0]
    return render(request, 'blog/index.html', {'posts': posts, 'last': last})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
