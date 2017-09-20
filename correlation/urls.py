from django.conf.urls import url

from . import views

app_name = 'correlation'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_upload$', views.post_form_upload, name='post_form_upload'),
]
