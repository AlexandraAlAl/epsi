from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.conf import settings
from django.core import management
import csv
import pprint
from django.contrib.auth.decorators import login_required
from extuser import models

#для регрессии
from pandas import read_csv
import sklearn.linear_model as lm



@login_required
def index(request):
    latest_post_list = Post.objects.order_by('-created_date').filter(author=request.user)
    context = {'latest_post_list': latest_post_list}
    return render(request, 'calculation/index.html', context)

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'calculation/detail.html', {'post': post})

@login_required
def archive(request):
    latest_post_list = Post.objects.order_by('-created_date').filter(author=request.user)
    archive_latest_post_list = latest_post_list.filter(delete_date='')
    context = {'archive_latest_post_list': archive_latest_post_list}
    return render(request, 'calculation/archive_index.html', context)

@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.file_name = post.file.name
            post.save()
            table = []
            table = handle_uploaded_file(request.FILES['file'])
            post.csi = count_csi(table)
            post.loyalty = count_loyalty(table)
            [post.one,post.two,post.three,post.four,post.five] = count_group(table)
            post.save()
            #
            tb = read_csv('mysite/media/calculation/' + request.FILES['file'].name,';')
    
            post.regress = regress(tb)
            post.save()
            return render(request, 'calculation/detail.html', {'post': post})
            #return redirect('/detail/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'calculation/new.html', {'form': form})

##@login_required
##def edit(request,post_id):
##    post = get_object_or_404(Post, pk=post_id)
##    if request.method == 'POST':
##        form = PostForm(request.POST, request.FILES, instance=post)
##        if form.is_valid():
##            #form.save()
##            post=form.save(commit=False)
##            post.author = request.user
##            post.created_date = timezone.now()
##            post.save()
##            file_field=request.FILES['file']
##            table = []
##            table = handle_uploaded_file(file_field)
##            #pprint.pprint(table)
##            post.csi = count_csi(table)
##            post.loyalty = count_loyalty(table)
##            [post.one,post.two,post.three,post.four,post.five] = count_group(table)
##            post.save()
##            
##            print(post.one,post.two,post.three,post.four,post.five)
##            return render(request, 'calculation/detail.html', {'post': post})
##            #return redirect('/detail/', pk=post.pk)
##    else:
##        form = PostForm(instance=post)
##    return render(request, 'calculation/edit.html', {'form': form})

"""считываем данные с загруженного файла"""
def handle_uploaded_file(f):
    """запись в новый файл
    url = 'mysite/media/' + request.user.myURL + '.csv'
    with open(url, 'wb+') as infile:
        for chunk in f.chunks():
            infile.write(chunk)
    """
    url = 'mysite/media/calculation/' + f.name
    myfile = open(url, 'r')
    table = []
    
    table = [row for row in csv.reader(myfile,delimiter=';')]
    myfile.close()


    for r in range(1,len(table)):
        for c in range(0, len(table[0])):
            table[r][c] =  float(table[r][c])
#считаем средние по столбцам и записываем их в конец таблицы
    row = [0.0]*len(table[0])
    for c in range(0, len(row)):
        s = 0
        k = 0
        for r in range(1, len(table)):
            k += 1
            s += table[r][c]
        row[c] = round(s*10/k, 1)
    table.append(row)
   
    return table

""" запись в файл не надо, не храним файлы
    outfile = open('mysite/media/example.csv', 'w')
    writer = csv.writer(outfile,delimiter=',')
    for row in table:
        writer.writerow(row)
    outfile.close()
"""

def count_csi(table):
    csi = 0
    r = len(table)
    for c in range(1, 4):
        csi += table[r-1][c-1]
    csi = csi/3
    return round(csi,0)

def count_loyalty(table):
    loyalty = 0
    r = len(table)
    for c in range(4, 7):
        loyalty += table[r-1][c-1]
    loyalty = loyalty/3
    return round(loyalty,0)

def count_group(table):
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    for r in range(1,len(table)-1):
        csi = 0
        loy = 0
        for c in range(0, 3):
            csi += table[r][c]
        csi = csi*10/3
        #print(csi)
        for c in range(3, 6):
            loy += table[r][c]
        loy = loy*10/3
        #print(loy)
        if csi <= 55:
            if loy <= 55:
                one += 1
                #print(1)
            else:
                three += 1
                #print(3)
        else:
            if loy <= 55:
                two += 1
                #print(2)
        if (loy>=75) and (csi>=75):
            four += 1
            #print(4)
    five = len(table)-2-one-two-three-four
    one = round(one/len(table)*100,1)
    two = round(two/len(table)*100,1)
    three = round(three/len(table)*100,1)
    four = round(four/len(table)*100,1)
    five = round(five/len(table)*100,1)
    return [one,two,three,four,five]




def regress(tb):
    x_csi = (tb['CSI1']+tb['CSI2']+tb['CSI3'])/3
    y_loy = (tb['Loyalty1']+tb['Loyalty2']+tb['Loyalty3'])/3
    x=x_csi.values.reshape(-1,1)
    y=y_loy.values.reshape(-1,1)
    # создаем пустую модель
    skm = lm.LinearRegression()
    # запускаем расчет параметров для указанных данных
    skm.fit(x, y)
    # и выведем параметры рассчитанной модели
    print(skm.intercept_, skm.coef_)
    return skm.coef_
