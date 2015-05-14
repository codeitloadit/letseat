from django.conf.urls import include, url

from restaurants import views


urlpatterns = [
    url(r'^/*$', views.index, name='index'),
    url(r'^new/*$', views.new, name='new'),
    url(r'^edit/(?P<pk>\d+)/*$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)/*$', views.delete, name='delete'),
]
