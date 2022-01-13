from . import views
from django.urls import path


urlpatterns = [
    path('subscribe.html/', views.newsletter_subscribe, name='subscribe_newsletters'),
    path('unsubscribe.html/', views.newsletter_unsubscribe, name='unsubscribe_newsletters'),
]

