from django.urls import path
from . import views


app_name = 'category_arab'

urlpatterns = [


path('<str:slug>', views.category_detail, name='category_detail'),




]
