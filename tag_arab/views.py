from inspect import BlockFinder
from pdb import post_mortem
from webbrowser import get

from django.forms import SlugField
from blog_arab.models import *
from django.shortcuts import render, redirect
from blog_arab.models import Blog
from index.forms import NewsletterUserSignUpForm
from index.models import MenuBarAr, MenuBarEn, NewsletterUser, FooterHeader
from .models import *
from django.db.models.aggregates import Count
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404


# Create your views here.
def tag_detail(request, slug):
    
    
    
    
    # ----------------------دالة الاشتراك في المدونة ----------------------------
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
# ----------------------------------------------------------------------------


# -------------------- الدالة الخاصة بعداد التعليقات---------------------
    #comment_count = Comment.objects.filter(post=Blog.objects.get(Slug=SlugField)).count()
#------------------------------------------------------------------


# --------------------دالة البحث -------------------------------
    search = Blog.objects.all()
    title = None
    if'search_name' in request.GET:
        title = request.GET['search_name']
        multiple_q = Q(Q(title__icontains=title) |
                       Q(content__icontains=title))
        search = search.filter(multiple_q)
#----------------------------------------------------


#--------------------دالة ترقيم الصفحات ---------------------------------
    paginator = Paginator(search, 8)  # Show 1 contacts per page.

    page_number = request.GET.get('page')

   
#-----------------------------------------------------------------------

   

   
   

    context = {
        'article': Blog.objects.filter(tag_ar=get_object_or_404(Tag, slug=slug)),#المسئول عن جلب المقالات من التاجات
        'tag':  get_object_or_404(Tag, slug=slug),#المسئول عن جلب المقالات من التاجات
        #'count_tag': Tag.objects.all().annotate(post_count=Count('post_tag')),
        'all_blogs': paginator.get_page(page_number),
        'all_category': Category.objects.all()[0:6],
        'about': AboutAuthor.objects.all()[:1],
        'popular_blogs': Blog.objects.all()[:4],
        'name_wedgits':  NameWidget.objects.all(),
        'ads': AdsWidget.objects.all()[:1],
        'cate_top': Blog.objects.filter(tag_ar=get_object_or_404(Tag, slug=slug))[:1],
        'form': form,
        'all_tags': Tag.objects.all(),
       'all_tag': Tag.objects.all()[0:6],
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],
        #'comment_count': comment_count,
        'FooterHeader': FooterHeader.objects.all()[:1],
    }
    
    return render(request, "pages\_tag_arab_blog.html", context)

    