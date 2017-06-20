from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

from . import views

urlpatterns = [

    url(r'^$', views.cart_home),
    url(r'^add/(?P<id>\d)/$', views.add_cart),
    url(r'^remove/(?P<id>\d)/$', views.remove_item),
    url(r'^checkout/$', views.view_cart),

]
