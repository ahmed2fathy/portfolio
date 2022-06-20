from django.urls import path
from . import views


app_name = 'blog_eng'

urlpatterns = [

    
    path('<str:slug>', views.single_blog, name='single_blog'),
    path('', views.blogs, name='all_blogs'),
   
   
    
    
   
   
]


