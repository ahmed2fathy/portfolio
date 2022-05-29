from django.urls import path
from . import views


app_name = 'BlogEn'

urlpatterns = [

    path('', views.blogs, name='all_blogs'),
    path('<slug:slug>', views.single_blog, name='single_blog')
]
