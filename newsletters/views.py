
# -*- coding: UTF-8 -*-

from django.contrib import messages
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm
from django.shortcuts import render
from django.core.mail import  send_mail
from django.conf import  settings
# Create your views here.

def newsletter_subscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None )
    
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
            
           

    context ={
        'form':form,
    
    }
    
    return render(request, 'newsletters/subscribe.html', context, )
    
    
    
def newsletter_unsubscribe(request):
    unsubscribe_form = NewsletterUserSignUpForm(request.POST or None)
    if unsubscribe_form.is_valid():
        instance = unsubscribe_form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Your Email has been removed', 
            'alert alert-success alert-dismissible')
            
            
            #send to email
            subject = " We will be very sad to leave "
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email, settings.EMAIL_HOST_USER]
            signup_message =""" We will be very sad to leave. if you would like to scribe visit http://127.0.0.1:8000/newsletters/subscribe.html/ ."""
            
            
            send_mail(subject = subject, from_email = from_email, recipient_list = to_email , message = signup_message, fail_silently = True )
            
            
        else:
            messages.warning(request, 'Your Email is not in data base', 
            'alert alert-warning alert-dismissible')
            
            
            
            
    context ={
        'form':unsubscribe_form ,
    
    }
    return render(request, 'newsletters/unsubscribe.html', context,)