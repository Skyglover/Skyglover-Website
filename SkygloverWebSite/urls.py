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
from home.views import about_page
from home.views import get_in_touch_page
from team.views import team_page
from projects import urls as projects_urls

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^projects/', include(projects_urls)),
    url(r'^team/$', team_page, name='team'),
    url(r'^about/$', about_page, name='about'),
    url(r'^get-in-touch/$', get_in_touch_page, name='get_in_touch'),
    url(r'^admin/', include(admin.site.urls)),
]
