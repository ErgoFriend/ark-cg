from django.urls import path,re_path
from . import views
app_name='home'
urlpatterns = [
    re_path(r'^', views.index, name='index'),
    re_path(r'^ark/contact', views.circle_contact, name="contact"),
    re_path(r'^ark/works', views.circle_works, name = 'works')
]
