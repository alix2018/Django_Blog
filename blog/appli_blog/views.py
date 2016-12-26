#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.http import Http404
from appli_blog.models import Article, Comment
from .forms import CommentForm

# Create your views here.


def accueil(request):
    """ Affiche les 5 derniers articles """
    articles = Article.objects.filter(is_visible=True).order_by('-date')[:3]
    return render(request, 'appli_blog/accueil.html', {'articles': articles})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    envoi = False
    
    # récupération des commentaires correspondants à l'article en cours de lecture
    commentaires = Comment.objects.filter(article=article, is_visible=True).order_by('date')

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CommentForm(request.POST)  # Nous reprenons les données
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
            comm = Comment(id=None, pseudo = form.cleaned_data['pseudo'], email = form.cleaned_data['email'], contenu = form.cleaned_data['contenu'], article = article)
            comm.save()
            envoi = True
            form = CommentForm()  # Nous créons un formulaire vide

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = CommentForm()  # Nous créons un formulaire vide

    return render(request, 'appli_blog/lire.html', {'article': article, 'commentaires':commentaires, 'form':form , 'envoi':envoi })