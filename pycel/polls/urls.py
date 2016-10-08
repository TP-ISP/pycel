from django.conf.urls import *
from polls import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
]
