from django.urls import path,re_path
from . import views
app_name='home'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact,name='contact'),
    path('works', views.works,name='works'),
    path('about_us', views.about_us,name='about_us'),
]
