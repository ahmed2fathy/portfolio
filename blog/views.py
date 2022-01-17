from contextlib import redirect_stdout
from itertools import count
from unicodedata import category
from django.http import request
from django.shortcuts import render, redirect
from index.forms import NewsletterUserSignUpForm
from index.views import all_index
from index.models import NewsletterUser
from .models import *
from django.db.models.aggregates import Count
from django.core.paginator  import Paginator
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
 
def  blog(request):
    
    
    form = NewsletterUserSignUpForm(request. POST or None )
    if form.is_valid():
        instance= form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already exists', 
            'alert alert-warning alert-dismissible')
           
        else:
             instance.save()
            
            #send to email
             subject = "Thank You For Joining  wibsite"
             from_email = settings.EMAIL_HOST_USER
             to_email = [instance.email, settings.EMAIL_HOST_USER]
             signup_message ="""Welcome to wibsite. if you would like to unscribe visit http://127.0.0.1:8000/newsletters/unsubscribe.html/ ."""
            
            
             send_mail(subject = subject, from_email = from_email, recipient_list = to_email , message = signup_message, fail_silently = True )
            
            
             messages.success(request, 'Your Email has been submitted', 
             'alert alert-success alert-dismissible')
    
    
    
    
    search= Blog.objects.all()
    title=None
    
    if'search_name'in request.GET:
            title= request.GET['search_name']
            if title:
                search= search.filter(title__icontains= title)
    
  
    
    paginator = Paginator(search, 2) # Show 1 contacts per page.
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    
    about = AboutAuthor.objects.all()[:1]
    popular_blogs = Blog.objects.all()[:4]
    name_wedgits = NameWidget.objects.all()
    ads = AdsWidget.objects.all()[:1]
    all_category = Category.objects.all().annotate(post_count=Count('post_category'))
    banner_category = Category.objects.all()[:3]
    all_tag = Tag.objects.all()[:10]
    
    
    context ={
    'all_blogs': page_obj,
    'about':about,
    'popular_blogs': popular_blogs,
    'name_wedgits':name_wedgits,
    'ads':ads,
    'all_category': all_category,
    'banner_category': banner_category,
    'form':form,
    'all_tag':all_tag,
    
    }
    
    return render(request,'pages/blog.html', context)
    
    
    
    
    
    
def single_blog(request, slug):
    single_blog = Blog.objects.get(slug=slug)
    
    
    form = NewsletterUserSignUpForm(request. POST or None )
    if form.is_valid():
        instance= form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already exists', 
            'alert alert-warning alert-dismissible')
           
        else:
             instance.save()
            
            #send to email
             subject = "Thank You For Joining  wibsite"
             from_email = settings.EMAIL_HOST_USER
             to_email = [instance.email, settings.EMAIL_HOST_USER]
             signup_message ="""Welcome to wibsite. if you would like to unscribe visit http://127.0.0.1:8000/newsletters/unsubscribe.html/ ."""
            
            
             send_mail(subject = subject, from_email = from_email, recipient_list = to_email , message = signup_message, fail_silently = True )
            
            
             messages.success(request, 'Your Email has been submitted', 
             'alert alert-success alert-dismissible')
    
    
    
    about = AboutAuthor.objects.all()[:1]
    popular_blogs = Blog.objects.all()[:4]
    name_wedgits = NameWidget.objects.all()
    ads = AdsWidget.objects.all()[:1]
    all_category = Category.objects.all().annotate(post_count=Count('post_category'))
    banner_category = Category.objects.all()[:3]
    all_tag = Tag.objects.all()[:10]
    
    
    
    
    context= {
    'single_blog':single_blog,
    'about':about,
    'popular_blogs': popular_blogs,
    'name_wedgits':name_wedgits,
    'ads':ads,
    'all_category': all_category,
    'banner_category': banner_category,
    'form':form,
    'all_tag':all_tag,
    
    }
    
    return render(request, 'pages\single-blog.html', context)
