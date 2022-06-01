from django.urls import path
from . import views


app_name = 'category_eng'

urlpatterns = [


path('<str:slug>', views.category_detail, name='category_detail'),




]
