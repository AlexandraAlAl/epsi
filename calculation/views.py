from django.http import Http404
from django.shortcuts import get_object_or_404,render
from .models import Post
from django.http import HttpResponse

def index(request):
    latest_post_list = Post.objects.order_by('-created_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'calculation/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'calculation/detail.html', {'post': post})

def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'calculation/detail.html', {'post': post})


