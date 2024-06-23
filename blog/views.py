from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    latest_post = Post.objects.filter(latest=True).first()
    other_posts = Post.objects.filter(latest=False).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'latest_post': latest_post, 'other_posts': other_posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})
