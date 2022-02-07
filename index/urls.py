from . import views
from django.urls import path


urlpatterns = [
    path('contact', views.feedback, name='feedback'),
    path('', views.all_index, name='all_index'),
    path('about', views.about_area, name='about_area'),
    path('service', views.service_area, name='service_area'),
    path('portfolio', views.portfolio_area, name='portfolio_area'),
]
