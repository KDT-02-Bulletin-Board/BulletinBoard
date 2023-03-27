from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def blog(request):
    postlist = Post.objects.all()
    context = {
        'postlist': postlist,
    }
    return render(request, 'main/blog.html', context)


def posting(request, num):
    post = Post.objects.get(pk=num)
    context = {
        'post': post,
        'pk':num,
    }
    return render(request, 'main/posting.html', context)