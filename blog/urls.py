from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [

path('', views.blog, name='all_blog'),
path('<slug:slug>' , views.single_blog, name='single_blog')
]
