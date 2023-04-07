# from django.shortcuts import render, redirect
from django.views.generic import ListView,  DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'
    
class PostDetail(DetailView):
    model = Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/index.html', {'posts':posts})

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post':post})

# def new(request):
#     return render(request, 'blog/new.html')

# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     post = Post(title=title, content=content)
#     post.save()
#     return redirect('blog:post_detail', post.pk)

