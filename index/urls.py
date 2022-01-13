from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_index, name='all_index')
]
