#-*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.text import Truncator
from appli_blog.models import Categorie, Article, Comment


# Création d'une classe pour chaque modèle

# Modèle pour les articles
class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter    = ('auteur','categorie', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    fields = ('titre', 'auteur', 'categorie', 'contenu')
    search_fields  = ('titre', 'contenu')


    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Apercu du contenu' # En-tête de la colonne


# Modèle pour les commentaires
class CommentAdmin(admin.ModelAdmin):
    list_display = ( 'pseudo', 'article', 'contenu', 'email', 'date', 'is_visible', )
    list_filter = ('article', 'pseudo', )
    search_fields = ('article', 'pseudo', )

# Pour prendre en compte ces modèles dans l'administration
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
