from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import NewsletterUserSignUpForm
from index.models import Brand, Call, ClientSay, FooterHeader, Hello, MySelf, NewsletterUser, Service, Tab, Work


# Create your views here.



def all_index(request):
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
            
    
    
    
    
    context = {
    'hello' : Hello.objects.all()[:1],
    'myself': MySelf.objects.all()[:1],
    'call': Call.objects.all()[:1],
    'service':Service.objects.all()[:4],
    'serv':Service.objects.all()[:1],
    'clientsay': ClientSay.objects.all()[:1],
    'client': ClientSay.objects.all(),
    'work': Work.objects.all(),
    'FooterHeader':FooterHeader.objects.all()[:1],
    'brand':Brand.objects.all()[:9],
    'work':Work.objects.all()[:1],
    'form':form,
    'alltabs': Tab.objects.all(),
    'Popular': Tab.objects.filter(status = 'Popular'),
    'Latest': Tab.objects.filter(status = 'Latest')[:6],
    'Following': Tab.objects.filter(status = 'Following')[:6],
    'Upcoming': Tab.objects.filter(status = 'Upcoming')[:6],
    }
    
    
    return render(request, 'pages/index.html', context)
    
    
    
   
    
