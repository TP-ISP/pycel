
from django.conf.urls import include, url
from django.contrib import admin
from pycel.view import *

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', hello),
    url(r'^login/', include('polls.urls')),
]
