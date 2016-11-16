from django.conf.urls import url
from . import views

app_name = 'ispproject'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.SelectView.as_view(), name='select'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
