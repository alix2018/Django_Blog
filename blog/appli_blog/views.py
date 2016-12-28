#-*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from django.http import Http404
from appli_blog.models import Article, Comment
from .forms import CommentForm


# Fonction qui affiche la liste des articles
def accueil(request):
    """ Affiche les 5 derniers articles """
    articles = Article.objects.filter(is_visible=True).order_by('-date')
    return render(request, 'appli_blog/accueil.html', {'articles': articles})


def lire(request, id):
    article = get_object_or_404(Article, id=id)
    envoi = False
    
    # Récupération des commentaires correspondants à l'article courant
    commentaires = Comment.objects.filter(article=article, is_visible=True).order_by('date')

    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CommentForm(request.POST)  # On récupère les données
        if form.is_valid(): # On vérifie que les données envoyées sont valides
            comm = Comment(id=None, pseudo = form.cleaned_data['pseudo'], email = form.cleaned_data['email'], contenu = form.cleaned_data['contenu'], article = article)
            comm.save()
            envoi = True
            form = CommentForm()  # On crée un formulaire vide

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = CommentForm()  # On crée un formulaire vide

    return render(request, 'appli_blog/lire.html', {'article': article, 'commentaires':commentaires, 'form':form , 'envoi':envoi })