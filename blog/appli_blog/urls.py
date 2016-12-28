#-*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from . import views,forms
admin.autodiscover()


# Les URLs du site : la page d'accueil, l'affichage d'un article et l'administration
urlpatterns = [ 
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    url(r'^admin/', include(admin.site.urls)),
]