"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from web import views

urlpatterns = [
    url(r'^containers/$', views.ListAll.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/$', views.Info.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/build_image/$', views.BuildImage.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/remove_image/$', views.RemoveImage.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/build_container/$', views.BuildContainer.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/remove_container/$', views.RemoveContainer.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/start/$', views.Start.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/stop/$', views.Stop.as_view()),
    url(r'^$', views.IndexTemplateView.as_view()),
    url(r'^admin/', admin.site.urls),
]
