from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

def index(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    last = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').reverse()[0]

    paginator = Paginator(post_list, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'posts': posts, 'last': last})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def sobre(request):
    return render(request, 'blog/sobre.html', {})

def busca(request):
    query = request.GET.get("q", None)
    blog = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    if query is not None:
        blog = blog.filter(
            Q(title__icontains=query) |
            Q(text__icontains=query) 
            )

    paginator = Paginator(blog, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/busca.html', {'posts': posts})