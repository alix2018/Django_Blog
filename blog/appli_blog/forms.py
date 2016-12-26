from appli_blog.models import ArticleForm
from django.shortcuts import render

def article(request):
	# Construit le formulaire soit vide soit avec les donnees existantes
	form = ArticleForm(request.POST or None)
	if form.is_valid(): 
		titre = form.cleaned_data['titre']
		contenu = form.cleaned_data['contenu']
		update = True
	return render(request, 'appli_blog/update_article.html', locals())
