from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^appli_blog/', include('appli_blog.urls')),
    url(r'^admin/', admin.site.urls),
]