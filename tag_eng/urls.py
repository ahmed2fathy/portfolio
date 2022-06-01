from django.urls import path
from . import views


app_name = 'tag_eng'

urlpatterns = [


    path('<str:slug>', views.tag_detail, name='tag_detail'),




]
