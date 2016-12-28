#-*- coding: utf-8 -*-


from django import forms
from .models import Comment

# Formulaire pour les commentaires
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pseudo', 'email', 'contenu']
