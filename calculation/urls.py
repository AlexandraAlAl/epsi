from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /calculation/
    url(r'^$', views.index, name='index'),
    # ex: /calculation/5/
    url(r'^(?P<calc_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /calculation/5/results/
    url(r'^(?P<calc_id>[0-9]+)/results/$', views.results, name='results'),
]
