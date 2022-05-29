
from pyexpat import model
from trace import Trace
from unicodedata import category
from xml.etree.ElementInclude import default_loader
from django.conf import Settings, settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
import blogs
import index
from urllib.parse import quote
from django.utils.encoding import iri_to_uri
from django.contrib import admin

from project.settings import LANGUAGE_CODE, LANGUAGES


# Create your models here.


class Tag(models.Model):
    name = models.CharField(
        max_length=80,    verbose_name=_('name'),)
    des = models.TextField(max_length=40, null=True,
                           blank=True, verbose_name=_('Description'),)
    image = models.ImageField(upload_to='media/blog/frontbage/tag',
                              null=True, blank=True, verbose_name=_('image'),)
    slug = models.SlugField(null=True, blank=True, verbose_name=_('url'),)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)  # Call the real save() method

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:single_blog', kwargs={'slug': self.slug})


class Category(models.Model):
    name = models.CharField(
        max_length=80,  verbose_name=_('name'),)
    des = models.TextField(max_length=40, null=True,
                           blank=True, verbose_name=_('Description'))
    image = models.ImageField(upload_to='media/blog/frontbage/category',
                              null=True, blank=True, verbose_name=_('image'))
    slug = models.SlugField(null=True, blank=True, verbose_name=_('url'))

    def __str__(self) -> str:
        return self.name


class Blogs(models.Model):

    title = models.CharField(
        max_length=200,  unique=True, verbose_name=_('title_en'))

    content = models.TextField(
        max_length=1000000,   verbose_name=_('content_en'))

    title_ar = models.CharField(
        max_length=200, unique=True, verbose_name=_('title_ar'))
    content_ar = models.TextField(
        max_length=100000, verbose_name=_('content_ar'))
    image = models.ImageField(
        upload_to='media/blog/frontbage', verbose_name=_('image'))
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name=_('created at'))
    author = models.ForeignKey(User, related_name='post_author',
                               default=User, on_delete=models.CASCADE, verbose_name=_(' author'))

    views = models.IntegerField(default=0,  verbose_name=_(' views'))
    slug = models.SlugField(max_length=200, blank=True, unique=True, help_text=_(
        'You should write some words indicating the content of the article in English'), verbose_name=_(' url'))

    def __str__(self):
        return '%s - %s' % (self.title, self.title_ar)

    class Meta:
        verbose_name_plural = _('Blogs')
        ordering = ["-created_at"]

    # دالة جلب رابط المقال

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogs:single_blog', kwargs={'slug': self.slug})

    #--------------------------------------------------------

     # دالة تحويل اسم المقال الي رابط وازالة المسافات الفارغة ووضع - داش

    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify(self.title)

        super(Blogs, self).save(*args, **kwargs)  # Call the real save() method

    #-----------------------------------------------------------------------------


class AboutAuthor(models.Model):
    image = models.ImageField(
        upload_to='media/blog/frontbage/about',  verbose_name=_('image'))
    name = models.CharField(
        max_length=70, default='user', verbose_name=_('name'))
    short_des = models.CharField(
        max_length=70, default='Senior blog writer', verbose_name=_('short description'))
    des = models.TextField(max_length=300, verbose_name=_('description'))
    fb_link = models.URLField(
        max_length=300, null=True, blank=True, verbose_name=_('Facebook link'))
    twitter_link = models.URLField(
        max_length=300, null=True, blank=True, verbose_name=_('Twitter link'))
    github_link = models.URLField(
        max_length=300, null=True, blank=True, verbose_name=_('Github link'))

    class Meta:
        verbose_name_plural = _('AboutAuthor')

    def __str__(self) -> str:
        return self.name


class NameWidget(models.Model):
    popular_post = models.CharField(
        max_length=90, default='Popular Posts', verbose_name=_('popular post'))
    post_catgories = models.CharField(
        max_length=90, default='Post Catgories', verbose_name=_('post catgories'))
    newsletter = models.CharField(
        max_length=90, default='Newsletter', verbose_name=_('newsletter'))
    tag_clouds = models.CharField(
        max_length=90, default='Tag Clouds', verbose_name=_(' tag clouds'))

    class Meta:
        verbose_name_plural = _('NameWidget')

    def __str__(self) -> str:
        return str('wedgit')


class AdsWidget(models.Model):
    ad_code_1 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (1) '))
    ad_code_2 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (2) '))
    ad_code_3 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (3) '))
    ad_code_4 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (4) '))
    ad_code_5 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (5) '))
    ad_code_6 = models.TextField(
        null=True, blank=True, default='Enter ads code', verbose_name=_(' ad code (6) '))

    class Meta:
        verbose_name_plural = _('AdsWidget')

    def __str__(self) -> str:
        return str('ad')


class Comment(models.Model):
    post = models.ForeignKey(Blogs, related_name='Comments',
                             on_delete=models.CASCADE, default='self', verbose_name=_('post'))
    name = models.CharField(max_length=70, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    body = models.TextField(max_length=500, verbose_name=_('comment'))
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name=_('date added'))

    class Meta:
        verbose_name_plural = _('Comments')

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class MenuBar(models.Model):
    menu = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name=_('name'))
    url = models.CharField(max_length=100, null=True, blank=True,
                           default='/', help_text="eg: /page", verbose_name=_('url'))

    class Meta:
        verbose_name_plural = _('MenuBar')

    def __str__(self) -> str:
        return self.menu
