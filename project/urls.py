"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns  # LANGUAGE_urlpatterns


# LANGUAGE_urlpatterns
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # LANGUAGE_url

]





urlpatterns += i18n_patterns  (
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
   
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name='index'),
   
    path('blog-en/', include('blog_eng.urls'), name='blog_eng'),
    path('category_en/', include('category_eng.urls'), name='category_eng'),
    path('tag_en/', include('tag_eng.urls'), name='tag_eng'),
    
    path('blog-ar/', include('blog_arab.urls'), name='blog_arab'),
    path('category_ar/', include('category_arab.urls'), name='category_arab'),
    path('tag_ar/', include('tag_arab.urls'), name='tag_arab'),
    path('newsletters/', include('newsletters.urls'), name='newsletters'),
    
)
    
    
    
   # path('about/', include('about.urls'), name='about'),
   # path('contact/', include('contact.urls'), name='contact'),
   # path('portfolio/', include('portfolio.urls'), name='portfolio'),
   # path('single_blog/', include('single_blog.urls'), name='single_blog'),
   # path('services/', include('services.urls'), name='services'),
    


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
