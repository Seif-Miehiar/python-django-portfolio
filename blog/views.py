from django.shortcuts import render
from blog.models import Post, Catagory


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts
    }
    return render(request, "blog_catagory.html", context)


def blog_detail(request):
    post = Post.object.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments
    }
    return render(request, "blog_detail.html", context)
