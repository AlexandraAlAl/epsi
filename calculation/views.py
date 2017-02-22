from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.conf import settings

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

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            handle_uploaded_file(request.FILES["file"])
            return render(request, 'calculation/detail.html', {'post': post})
            #return redirect('/detail/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'calculation/new.html', {'form': form})


def edit(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            #form.save()
            post=form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            file_field=request.FILES['file']
            handle_uploaded_file(file_field)
            return render(request, 'calculation/detail.html', {'post': post})
            #return redirect('/detail/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'calculation/edit.html', {'form': form})


def handle_uploaded_file(f):
    with open('calculation/data.txt', 'wb+') as dest:
        for chunk in f.chunks():
            dest.write(chunk)


