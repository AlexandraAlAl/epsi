from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /posts/
    url(r'^$', views.index, name='index'),
    # ex: /posts/5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /posts/5/results/
    url(r'^(?P<post_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /posts/new/
    url(r'^new/$', views.new, name='new'),
    # ex: /posts/5/edit/
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
