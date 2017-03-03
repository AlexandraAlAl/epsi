from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /5/
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /5/results/
    url(r'^(?P<post_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /new/
    url(r'^new/$', views.new, name='new'),
    # ex: /5/edit/
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name='edit'),
]
