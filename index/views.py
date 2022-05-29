from http.client import HTTPResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import BadHeaderError
from django.shortcuts import redirect, render

from .forms import FeedbackForm, NewsletterUserSignUpForm
from index.models import MenuBarAr, MenuBarEn, Skills, Call, ClientSay, ContactInfo,  FooterHeader, Hello, MySelf, NewsletterUser, Service, Tab, Work



#

# Create your views here.
    

# دالة فيد باك----------------------------
from .forms import FeedbackForm
from django.core.mail import mail_admins

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)

        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(
                f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')

    else:
        f = FeedbackForm()
        
        
    context = {
    'formx': f,
    'FooterHeader': FooterHeader.objects.all()[:1],
    'menu_ar': MenuBarAr.objects.all()[:8],
    'menu_en': MenuBarEn.objects.all()[:8],
    'ContactInfo': ContactInfo.objects.all(),
    }
    
    
    return render(request, 'pages/contact.html', context)
#---------------------------------------------------------



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
    'skills':Skills.objects.all()[:9],
    'work':Work.objects.all()[:1],
    'form':form,
    'alltabs': Tab.objects.all(),
    'Popular': Tab.objects.filter(status = 'Popular'),
    'Latest': Tab.objects.filter(status = 'Latest')[:6],
    'Following': Tab.objects.filter(status = 'Following')[:6],
    'Upcoming': Tab.objects.filter(status = 'Upcoming')[:6],
    'menu_ar': MenuBarAr.objects.all()[:8],
    'menu_en': MenuBarEn.objects.all()[:8],
    
    
    }
    
    
    return render(request, 'pages/index.html', context)
    
    
    
    
def about_area(request):
    form = NewsletterUserSignUpForm(request. POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already exists',
                             'alert alert-warning alert-dismissible')

        else:
            instance.save()

            #send to email
            subject = "Thank You For Joining  wibsite"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email, settings.EMAIL_HOST_USER]
            signup_message = """Welcome to wibsite. if you would like to unscribe visit http://127.0.0.1:8000/newsletters/unsubscribe.html/ ."""

            send_mail(subject=subject, from_email=from_email,
                      recipient_list=to_email, message=signup_message, fail_silently=True)

            messages.success(request, 'Your Email has been submitted',
                             'alert alert-success alert-dismissible')

    context = {
        'hello': Hello.objects.all()[:1],
        'myself': MySelf.objects.all()[:1],
        'call': Call.objects.all()[:1],
        'service': Service.objects.all()[:4],
        'serv': Service.objects.all()[:1],
        'clientsay': ClientSay.objects.all()[:1],
        'client': ClientSay.objects.all(),
        'work': Work.objects.all(),
        'FooterHeader': FooterHeader.objects.all()[:1],
        'skills': Skills.objects.all()[:9],
        'work': Work.objects.all()[:1],
        'form': form,
        'alltabs': Tab.objects.all(),
        'Popular': Tab.objects.filter(status='Popular'),
        'Latest': Tab.objects.filter(status='Latest')[:6],
        'Following': Tab.objects.filter(status='Following')[:6],
        'Upcoming': Tab.objects.filter(status='Upcoming')[:6],
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],

    }

    return render(request, 'pages/about.html', context)
    
    
    
def service_area(request):
    form = NewsletterUserSignUpForm(request. POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already exists',
                             'alert alert-warning alert-dismissible')

        else:
            instance.save()

            #send to email
            subject = "Thank You For Joining  wibsite"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email, settings.EMAIL_HOST_USER]
            signup_message = """Welcome to wibsite. if you would like to unscribe visit http://127.0.0.1:8000/newsletters/unsubscribe.html/ ."""

            send_mail(subject=subject, from_email=from_email,
                      recipient_list=to_email, message=signup_message, fail_silently=True)

            messages.success(request, 'Your Email has been submitted',
                             'alert alert-success alert-dismissible')

    context = {
        'hello': Hello.objects.all()[:1],
        'myself': MySelf.objects.all()[:1],
        'call': Call.objects.all()[:1],
        'service': Service.objects.all()[:4],
        'serv': Service.objects.all()[:1],
        'clientsay': ClientSay.objects.all()[:1],
        'client': ClientSay.objects.all(),
        'work': Work.objects.all(),
        'FooterHeader': FooterHeader.objects.all()[:1],
        'skills': Skills.objects.all()[:9],
        'work': Work.objects.all()[:1],
        'form': form,
        'alltabs': Tab.objects.all(),
        'Popular': Tab.objects.filter(status='Popular'),
        'Latest': Tab.objects.filter(status='Latest')[:6],
        'Following': Tab.objects.filter(status='Following')[:6],
        'Upcoming': Tab.objects.filter(status='Upcoming')[:6],
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],

    }

    return render(request, 'pages/services.html', context)
    
    
def portfolio_area(request):
    form = NewsletterUserSignUpForm(request. POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'Your Email Already exists',
                             'alert alert-warning alert-dismissible')

        else:
            instance.save()

            #send to email
            subject = "Thank You For Joining  wibsite"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email, settings.EMAIL_HOST_USER]
            signup_message = """Welcome to wibsite. if you would like to unscribe visit http://127.0.0.1:8000/newsletters/unsubscribe.html/ ."""

            send_mail(subject=subject, from_email=from_email,
                      recipient_list=to_email, message=signup_message, fail_silently=True)

            messages.success(request, 'Your Email has been submitted',
                             'alert alert-success alert-dismissible')

    context = {
        'form': form,
        'work': Work.objects.all()[:1],
        'alltabs': Tab.objects.all(),
        'Popular': Tab.objects.filter(status='Popular'),
        'Latest': Tab.objects.filter(status='Latest')[:6],
        'Following': Tab.objects.filter(status='Following')[:6],
        'Upcoming': Tab.objects.filter(status='Upcoming')[:6],
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],
        'FooterHeader': FooterHeader.objects.all()[:1],

    }

    return render(request, 'pages/portfolio.html', context)
    
    
    
 