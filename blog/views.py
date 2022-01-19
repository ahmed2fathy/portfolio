from next_prev import next_in_order, prev_in_order
from .forms import CommentForm
from django.http import request
from django.shortcuts import render, redirect
from index.forms import NewsletterUserSignUpForm
from index.models import NewsletterUser
from .models import *
from django.db.models.aggregates import Count
from django.core.paginator  import Paginator
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404

# Create your views here.



 
def  blog(request):
    
    # دالة الاشتراك في المدونة
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
             # -------------------------------------------------------
    
    
    # دالة البحث
    search= Blog.objects.all()
    title=None
    if'search_name' in request.GET:
            title= request.GET['search_name']
            multiple_q =  Q(Q(title__icontains = title) |
                            Q(content__icontains = title))
            search= search.filter(multiple_q)
              #-------------------------------  
  
  
    #دالة ترقيم الصفحات
    paginator = Paginator(search, 2) # Show 1 contacts per page.
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    #-----------------------------------------
   
    
    
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
    'single_blog':single_blog,
    
    }
    
    return render(request,'pages/blog.html', context)
    
    
    
    
    
    #----------------------------------------------------------------
def single_blog(request, slug):

    single_blog = Blog.objects.get(slug=slug)
    
    # عداد الزيارات
    single_blog.views = single_blog.views + 1
    single_blog.save()
    #-------------------------
    
    
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
    
    
    
    #فورم التعليقات  CommentForm
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.blog = Blog.objects.get(slug=slug)
            obj.save()
            return redirect('blog:single_blog', slug=single_blog.slug)
            
    else:
        comment_form = CommentForm() 
        
    #-------------------------------------------
    
        
    about = AboutAuthor.objects.all()[:1]
    popular_blogs = Blog.objects.all()[:4]
    name_wedgits = NameWidget.objects.all()
    ads = AdsWidget.objects.all()[:1]
    all_category = Category.objects.all().annotate(post_count=Count('post_category'))
    banner_category = Category.objects.all()[:3]
    all_tag = Tag.objects.all()[:10]
    
    
       
    # دالة عرض ذر السابق والتالي في المقال
    post = get_object_or_404(Blog, slug=slug)
    try:
        next_post = post.get_next_by_created_at()
    except Blog.DoesNotExist:
        next_post= None

    try:
        previous_post = post.get_previous_by_created_at()
    except Blog.DoesNotExist:
        previous_post = None
    #-----------------------------------------------------
   


   
      
    
    
    
    
    
    context= {
   
    'post': post,
    'next_post': next_post,
    'previous_post': previous_post,
    
    
    
    'single_blog':single_blog,
    'about':about,
    'popular_blogs': popular_blogs,
    'name_wedgits':name_wedgits,
    'ads':ads,
    'all_category': all_category,
    'banner_category': banner_category,
    'form':form,
    'all_tag':all_tag,
    'comment_form':comment_form,

   
    }
    
    return render(request, 'pages\single-blog.html', context)
