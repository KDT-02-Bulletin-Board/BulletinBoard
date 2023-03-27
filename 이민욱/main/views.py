from django.shortcuts import render,redirect
from .models import Post

# Create your views here.

app_name = 'main'
def best(request):
    postlist = Post.objects.all()
    return render(request, 'best/best.html', {'postlist':postlist})

def detail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    return render(request, 'best/detail.html', {'post':post_detail})

def write(request):
    if request.method == 'POST':
        write = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.POST['author'],
        )
        return redirect('main:best')
    return render(request, 'best/write.html')
