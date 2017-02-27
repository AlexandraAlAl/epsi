from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.conf import settings
from django.core import management
import csv
import pprint

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
            table = []
            table = handle_uploaded_file(request.FILES['file'])
            
            csi = 0
            for c in range(1, 4):
                print(c-1)
                print(len(table)-1)
                r = len(table)
                print(table[r-1][c-1])
                csi += table[r-1][c-1]
                print(csi)
            post.csi = round(csi,2) 
            post.save()

            loyalty = 0
            for c in range(4, 7):
                print(c-1)
                print(len(table)-1)
                r = len(table)
                print(table[r-1][c-1])
                loyalty += table[r-1][c-1]
                print(loyalty)
            post.loyalty = round(loyalty,2)
            post.save()
            
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
            table = []
            table = handle_uploaded_file(file_field)
            
            csi = 0
            for c in range(1, 4):
                print(c-1)
                print(len(table)-1)
                r = len(table)
                print(table[r-1][c-1])
                csi += table[r-1][c-1]
                print(csi)
            post.csi = round(csi/3,2)

            loyalty = 0
            for c in range(4, 7):
                print(c-1)
                print(len(table)-1)
                r = len(table)
                print(table[r-1][c-1])
                loyalty += table[r-1][c-1]
                print(loyalty)
            post.loyalty = round(loyalty/3,2)
            post.save()
            
            return render(request, 'calculation/detail.html', {'post': post})
            #return redirect('/detail/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'calculation/edit.html', {'form': form})


def handle_uploaded_file(f):
    with open('calculation/data.csv', 'wb+') as infile:
        for chunk in f.chunks():
            infile.write(chunk)
    infile = open('calculation/data.csv', 'r')
    table = []
    table = [row for row in csv.reader(infile,delimiter=';')]
    infile.close()

    for r in range(1,len(table)):
        for c in range(0, len(table[0])):
            table[r][c] =  float(table[r][c])

    row = [0.0]*len(table[0])
    for c in range(0, len(row)):
        s = 0
        k = 0
        for r in range(1, len(table)):
            k += 1
            s += table[r][c]
        row[c] = round(s/k, 1)
    table.append(row)

    outfile = open('calculation/data.csv', 'w')
    writer = csv.writer(outfile,delimiter=',')
    for row in table:
        writer.writerow(row)
    outfile.close()
    pprint.pprint(table)
    return table

   

def count(request,post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'calculation/detail.html', {'post': post})
