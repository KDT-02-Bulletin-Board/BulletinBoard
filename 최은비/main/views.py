from django.shortcuts import render
from django.shortcuts import redirect
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
    }
    return render(request, 'main/posting.html', context)


def new_post(request):
    if request.method == "POST":
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, num):
    post = Post.objects.get(pk=num)
    context = {
        'post': post,
    }
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', context)