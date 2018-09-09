"""MyDjangoProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from HelloDjango import views as myViews

urlpatterns = [
    path('', myViews.Index),
    path('add/', myViews.Add, name='add'),
    path('admin/', admin.site.urls),
    url(r'^login/$', myViews.Login),
    url(r'^loginHandle/$', myViews.LoginHandle),
    url(r'^home/$', myViews.Home),
    url(r'^hello/$', myViews.HelloWorld),
    url(r'^weather/$', myViews.Weather),
    url(r'^restful/$', myViews.Restful),
    url(r'^redirection/$', myViews.Redirection),
]
