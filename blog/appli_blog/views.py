#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from appli_blog.models import Article


# Create your views here.


def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'appli_blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'appli_blog/lire.html', {'article':article})

def date_actuelle(request):
    return render(request, 'appli_blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'appli_blog/addition.html', locals())