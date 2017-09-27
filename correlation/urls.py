from django.conf.urls import url

from . import views

app_name = 'correlation'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form_upload$', views.post_form_upload, name='post_form_upload'),
    url(r'^post_result$', views.post_result, name='post_result'),
    url(r'^registration_form$', views.UserFormView.as_view(), name='registration_form'),

]
