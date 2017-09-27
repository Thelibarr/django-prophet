from django.conf.urls import url, include
from . import views

from django.contrib.auth.views import login

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),

]
