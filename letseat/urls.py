"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView, TemplateView

from letseat import views
from restaurants import urls as restaurant_urls

urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    url(r'^accounts/login/*$', RedirectView.as_view(url='/login_or_register', permanent=True)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^restaurants/', include(restaurant_urls, namespace='restaurants')),

    url(r'^/*$', views.index, name='index'),
    url(r'^register/*$', views.register, name='register'),
    url(r'^login_or_register/*$', views.login_or_register, name='login_or_register'),
    url(r'^login/*$', views.login, name='login'),
    url(r'^logout/*$', views.logout, name='logout'),
    url(r'^home/*$', views.home, name='home'),
]
