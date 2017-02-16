from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-created_date')[:5]
    template = loader.get_template('calculation/index.html')
    context = RequestContext(request, {
        'latest_post_list': latest_post_list,
    })
    return HttpResponse(template.render(context))

def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)

def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)
