#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from django.db import models

# Composition d'un article
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=30)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de publication")
    categorie = models.ForeignKey('Categorie')
    is_visible = models.BooleanField(verbose_name="Article publié ?", default=True)

    def __str__(self):
        return self.titre

# Clé étrangère : catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


# Composition d'un commentaire
class Comment(models.Model):
    pseudo = models.CharField(max_length=50, null=False, verbose_name="Pseudo")
    email = models.EmailField(max_length=50, verbose_name="Email")
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date du commentaire", auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Commentaire publie ?", default=True)
    article = models.ForeignKey('Article')
    
    def __str__(self):
        return self.pseudo
