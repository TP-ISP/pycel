from django.conf.urls import url
from . import views

app_name = 'ispproject'
urlpatterns = [
    url(r'^select/$', views.SelectView.as_view(), name='select'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^detail/(?P<project_id>[0-9]+)/$', views.ProjectDetailView.as_view(), name='detail'),
]
