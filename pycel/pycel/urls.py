
from django.conf.urls import include, url
from django.contrib import admin
from pycel.view import hello

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^hello/$', hello),
]
