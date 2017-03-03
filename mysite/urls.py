from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^accounts/login/profile/edit/', views.profile_edit, name='profile_edit'),
    url(r'^accounts/login/profile/', views.profile, name='profile'),
    url(r'^accounts/login/', views.login, name='login'),    
    url(r'^accounts/logout/', views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<user_name>[a-z]+)/', include('calculation.urls', namespace="calculation"), name='user'),
    url(r'', include('calculation.urls', namespace="calculation")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
