from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.contrib import admin
from pycel.views import *
from . import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', hello),
    url(r'polls/', include('polls.urls')),
]

urlpatterns += staticfiles_urlpatterns()
