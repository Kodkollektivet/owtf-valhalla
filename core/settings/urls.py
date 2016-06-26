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
    url(r'^containers/buildall/$', views.BuildAll.as_view()),
    url(r'^containers/rebuildall/$', views.RebuildAll.as_view()),
    url(r'^containers/stopall/$', views.StopAll.as_view()),
    url(r'^containers/commands/$', views.Commands.as_view()),    
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/$', views.Info.as_view()),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/build/$', views.Build.as_view(), name='build'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/remove/$', views.Remove.as_view(), name='remove'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/build_image/$', views.BuildImage.as_view(), name='build_image'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/remove_image/$', views.RemoveImage.as_view(), name='remove_image'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/build_container/$', views.BuildContainer.as_view(), name='build_container'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/remove_container/$', views.RemoveContainer.as_view(), name='remove_container'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/start/$', views.Start.as_view(), name='start'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/stop/$', views.Stop.as_view(), name='stop'),
    url(r'^containers/(?P<image>[a-zA-z0-9:.]+)/execute/$', views.Execute.as_view(), name='execute'),
    url(r'^$', views.IndexTemplateView.as_view()),
    url(r'^admin/', admin.site.urls),
]
