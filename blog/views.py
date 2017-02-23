from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', locals())

def post_detail(request, pk):   # primary key
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', locals())

def post_new(request):
    if request.method == 'POST':
        pass
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', locals())
