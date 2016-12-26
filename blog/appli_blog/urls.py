from django.conf.urls import url, include
from django.contrib import admin
from . import views,forms



urlpatterns = [
	# blog 
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^update/$', forms.article, name='article'),
    # tests
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition)
]