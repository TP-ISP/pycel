from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from pycel.view import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', hello),
    url(r'^login/', include('login.urls')),
]

urlpatterns += staticfiles_urlpatterns()
