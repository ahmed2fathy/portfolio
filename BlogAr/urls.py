from django.urls import path
from . import views


app_name = 'BlogAr'

urlpatterns = [

    path('', views.blogs, name='all_blogs'),
    path('<str:slug>', views.single_blog, name='single_blog')
]
