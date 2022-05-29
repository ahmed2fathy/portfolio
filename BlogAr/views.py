

from inspect import BlockFinder
from pdb import post_mortem

from django.forms import SlugField
from .forms import CommentForm
from django.shortcuts import render, redirect
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


def blogs(request):

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
    search = Blogs.objects.all()
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

    page_obj = paginator.get_page(page_number)
#-----------------------------------------------------------------------

    about = AboutAuthor.objects.all()[:1]
    popular_blogs = Blogs.objects.all()[:4]
    name_wedgits = NameWidget.objects.all()
    ads = AdsWidget.objects.all()[:1]
   # all_category = Category.objects.all().annotate(post_count=Count('post_category'))
    #banner_category = Category.objects.all()[:3]
   # all_tag = Tag.objects.all()[:10]
   

    context = {
        'top_blogs': Blogs.objects.all()[1:2],
        'all_blogs': page_obj,
        'all_category': Category.objects.all()[0:6],
        'about': about,
        'popular_blogs': popular_blogs,
        'name_wedgits': name_wedgits,
        'ads': ads,
        #'all_category': all_category,
        #'banner_category': banner_category,
        'form': form,
        'all_tag': Tag.objects.all()[0:6],
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],
        #'comment_count': comment_count,
        'FooterHeader': FooterHeader.objects.all()[:1],
    }

    return render(request, 'pages/blogs-ar.html', context)

    #----------------------------------------------------------------


def single_blog(request, slug):

    single_blog = Blogs.objects.get(slug=slug)

# -------------------- الدالة الخاصة بعداد التعليقات---------------------
    comment_count = Comment.objects.filter(
        post=Blogs.objects.get(slug=slug)).count()
#------------------------------------------------------------------

# ---------------- عداد الزيارات ------------------------
    single_blog.views = single_blog.views + 1
    single_blog.save()
#----------------------------------------------------

# ----------------- دالة عرض ذر السابق والتالي في المقال ----------------------
    post = get_object_or_404(Blogs, slug=slug)
    try:
        next_post = post.get_next_by_created_at()
    except Blogs.DoesNotExist:
        next_post = None

    try:
        previous_post = post.get_previous_by_created_at()
    except Blogs.DoesNotExist:
        previous_post = None
#---------------------------------------------------------------


#------------------ فورم التعليقات  CommentForm ---------------
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.post = Blogs.objects.get(slug=slug)
            obj.save()
            return redirect('blogs:single_blog', slug=single_blog.slug)

    else:
        comment_form = CommentForm()

#---------------------------------------------

 # -----------------دالة الاشتراك في المدونة -----------------
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
#--------------------------------------------------------------------------------------

    about = AboutAuthor.objects.all()[:1]
    popular_blogs = Blogs.objects.all()[:4]
    name_wedgits = NameWidget.objects.all()
    ads = AdsWidget.objects.all()[:1]
   # all_category = Category.objects.all().annotate(post_count=Count('post_category'))
    #banner_category = Category.objects.all()[:3]
    #all_tag = Tag.objects.all()[:10]
  

    context = {

        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
        'single_blog': single_blog,
        'about': about,
        'popular_blogs': popular_blogs,
        'name_wedgits': name_wedgits,
        'ads': ads,
        #'all_category': all_category,
        #'banner_category': banner_category,
        'form': form,
        #'all_tag': all_tag,
        'comment_form': comment_form,
        'comment_count': comment_count,
        'menu_ar': MenuBarAr.objects.all()[:8],
        'menu_en': MenuBarEn.objects.all()[:8],
        'FooterHeader': FooterHeader.objects.all()[:1],

    }

    return render(request, 'pages\single-blog-ar.html', context)


#--------------------------------------------------------------------------------------
