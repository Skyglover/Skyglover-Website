"""SkygloverWebSite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_page
from projects.views import projects_page
from projects.views import project_details_page
from team.views import team_page


urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^projects/$', projects_page, name='projects'),
    url(r'^projects/(?P<project_name_slug>[-\w]+)/$', project_details_page, name='project_details'),
    url(r'^team/$', team_page, name='team'),
    url(r'^admin/', include(admin.site.urls)),
]
