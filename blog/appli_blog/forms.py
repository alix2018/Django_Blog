#-*- coding: utf-8 -*-


from django import forms
from .models import Comment

# create the form class.
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pseudo', 'email', 'contenu']
