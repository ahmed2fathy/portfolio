
# -*- coding: UTF-8 -*-

from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class NewsletterUser(models.Model):
    email= models.EmailField( verbose_name=_('email'))
    data_added = models.DateTimeField(
        auto_now_add=True, verbose_name=_('data_added'))
    
    class Meta:
        verbose_name_plural = _('NewsletterUser')
    
    def __str__(self) -> str:
        return self.email

class FooterHeader(models.Model):
    site_name = models.CharField(
        max_length=220, blank=True, verbose_name=_('site_name'))
    logo                = models.ImageField (upload_to = 'media/index/FollowMe/',null = True , blank = True, verbose_name=_('logo'))
    phone               = models.CharField(max_length = 20, null = True , blank = True, verbose_name=_('phone'))
    address             = models.CharField(max_length = 300, null = True , blank = True, verbose_name=_('address'))
    email               = models.EmailField(max_length = 254, null = True , blank = True, verbose_name=_('email'))
    description         = models.TextField(max_length = 500, null = True , blank = True, verbose_name=_('description'))
    follow_me_text_name = models.CharField(max_length = 220, null = True , blank = True, default='follow_me_text_name')
    fb_link             = models.URLField(max_length = 600,  null = True , blank = True, verbose_name=_('fb_link'))
    twitter_link = models.URLField(
        max_length=600, null=True, blank=True, verbose_name=_('twitter_link'))
    github_link      = models.URLField(max_length = 600,  null = True , blank = True, verbose_name=_('github_link'))
    Copyright           = models.CharField(max_length = 220, null = True , blank = True, default='Copyright', verbose_name=_('Copyright'))
    all_rights_reserved = models.CharField(
        max_length=220, null=True, blank=True, default=' All rights reserved', verbose_name=_('all_rights_reserved'))
    Copyright_txt_1     = models.CharField(max_length = 220, null = True , blank = True, default='This template is made with', verbose_name=_('Copyright_txt_1'))
    Copyright_txt_2     = models.CharField(max_length = 220, null = True , blank = True,default='by', verbose_name=_('Copyright_txt_2'))
    Copyright_link = models.URLField(
        max_length=400, null=True, blank=True, verbose_name=_('Copyright_link'))
    Copyright_date = models.DateTimeField(
        default=timezone.now, verbose_name=_('Copyright_date'))
    
    class Meta:
        verbose_name_plural = _('FooterHeader')
    
    
    def  __str__(self):
        return "setting footer and header - "  + str(self.id)
        
    


class Hello(models.Model):
    hello_name = models.CharField(
        max_length=50,  default='hello', verbose_name=_('hello_name'))
    title = models.CharField(max_length=50 , blank = True, verbose_name=_('title'))
    des = models.TextField(max_length=400, blank=True, verbose_name=_('des'))
    image_banner = models.ImageField(
        upload_to='media/index/hello/', null=True, blank=True, verbose_name=_('image_banner'))
    cv = models.CharField(max_length=50,  default='Get CV', verbose_name=_('cv'))
    cv_link = models.URLField(
        max_length=2000, null=True, blank=True, verbose_name=_('cv_link'))
    hire = models.CharField(
        max_length=50,  default='Hire Me', verbose_name=_('hire'))
    hire_link = models.URLField(
        max_length=2000, null=True, blank=True, verbose_name=_('hire_link'))
    back_banner = models.ImageField(upload_to='media/index/hello/' ,null = True , blank = True, verbose_name=_('back_banner'))
    phone = models.CharField(max_length=50, blank=True,
                             verbose_name=_('phone'))
    
    class Meta:
        verbose_name_plural = _('Hello')
    
    def __str__(self):
            return self.hello_name
        
        
        
class MySelf(models.Model):
    title = models.CharField(max_length=50 , verbose_name=_('title'))
    des= models.TextField(max_length=400, blank = True, verbose_name=_('des') )
    download_cv = models.CharField(max_length=50,  default=' Download CV', verbose_name=_('download_cv'))
    download_link = models.URLField(max_length = 2000, null = True , blank = True , verbose_name=_('download_link'))
    image = models.ImageField(
        upload_to='media/index/myself/', null=True, blank=True, verbose_name=_('image'))
    
    class Meta:
        verbose_name_plural = _('MySelf')
    
    def __str__(self) -> str:
        return self.title



class Call(models.Model):
    title = models.CharField(max_length=50,default='call us now', verbose_name=_('title'))
    des = models.TextField(max_length=400,  null = True , blank = True, verbose_name=_('des'))
    image = models.ImageField(upload_to='media/index/call/' , null = True , blank = True, verbose_name=_('image'))
    phone = models.CharField(max_length=50, null = True , blank = True , verbose_name=_('phone'))
    experience = models.CharField(max_length=60, default=' Years Experience Working',
                                  null=True, blank=True, verbose_name=_('experience'))
    years = models.IntegerField(
        default='3', null=True, blank=True, verbose_name=_('years'))
    
    class Meta:
        verbose_name_plural = _('Call')
   
    def __str__(self) -> str:
        return self.title
        
        
     
class Service(models.Model):
    big_name = models.CharField(max_length=50, null = True , blank = True, verbose_name=_('big_name'))
    big_dec = models.TextField(
        max_length=300, null=True, blank=True, verbose_name=_('big_dec'))
    title= models.CharField(max_length=50, verbose_name=_('title'))
    des = models.TextField(max_length=400, verbose_name=_('des'))
    image = models.ImageField(
        upload_to='media/index/service/', verbose_name=_('image'))
        
    class Meta:
        verbose_name_plural = _('Service')
    
    def __str__(self) -> str:
        return self.title
        
        

class Work(models.Model):
    
    title = models.CharField(max_length=50, verbose_name=_('title'))
    des = models.TextField(max_length=300, null=True,
                           blank=True, verbose_name=_('des'))
    class Meta:
        verbose_name_plural = _('Work')
    
    def __str__(self) -> str:
            return self.title
            
    
class Tab(models.Model):
    status_tab= [
    ('Popular','Popular'),
    ('Latest','Latest'),
    ('Following','Following'),
    ('Upcoming','Upcoming'),
    ]
    status = models.CharField(max_length=50 , choices=status_tab, null=True, blank = True, verbose_name=_('status'))
    title = models.CharField(max_length=50, null = True , blank = True, verbose_name=_('title'))
    des = models.TextField(max_length=300, null = True , blank = True, verbose_name=_('des'))
    image = models.ImageField(upload_to='media/index/work/popular/',
                              null=True, blank=True, verbose_name=_('image'))
    active = models.BooleanField(default=True, verbose_name=_('active'))
    
    class Meta:
        verbose_name_plural = _('Tab')
        
    def __str__(self) -> str:
            return self.title

        
        
class ClientSay(models.Model):
    big_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_('big_name'))
    big_dec = models.TextField(max_length=300, null = True , blank = True, verbose_name=_('big_dec'))
    title= models.CharField(max_length=60, verbose_name=_('title'))
    des = models.TextField(max_length=400, verbose_name=_('des'))
    image = models.ImageField(
        upload_to='media/index/clientsay/', verbose_name=_('image'))
        
    class Meta:
        verbose_name_plural = _('ClientSay')
    
    def __str__(self) -> str:
        return self.title
     
            
class Skills(models.Model):
    color = [
        ('#800000', 'Maroon'),
        ('#728FCE', 'LightPurple'),
        ('#800080', 'Purple'),
        ('#4863A0', 'Azure'),
        ('#566D7E', 'Marble'),
        ('#CD7F32', ' Bronze'),
        ('#FF8040', 'Orange'),
        ('#15317E ', 'Lapis'),
        ('#1E90FF', 'DeepSkyBlue'),
        ('#0041C2', '  Canary'),
        ('#7BCCB5', 'BlueGreen'),
        ('#6A5ACD', 'SlateBlue'),
        ('#8A2BE2 ', 'BlueViolet'),
        ('#57FEFF', 'Zircon'),
    ]
    skill_title = models.CharField(max_length=60, verbose_name=_('skill_title'))
    skill_percentage = models.IntegerField(verbose_name=_('skill_percentage'))
    image = models.ImageField(
        upload_to='media/index/Skill/', verbose_name=_('image'))
    color_bar = models.CharField(max_length=60,choices =color, verbose_name=_('color') )
    def __str__(self) -> str:
        return str(self.skill_title)

    class Meta:
        verbose_name_plural = _('skills')
     

class Feedback(models.Model):
    name = models.CharField(
        max_length=200, verbose_name=_('name'), help_text="")
    email = models.EmailField(max_length=200, verbose_name=_('email'))
    subject = models.CharField(max_length=200, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))

    class Meta:
        verbose_name_plural = _('Feedback')

    def __str__(self):
        return self.name + "-" + self.email
        
        
class ContactInfo(models.Model):
    address             = models.CharField(max_length = 70, null = True , blank = True, verbose_name=_('address'))
    address_details     = models.CharField(max_length = 90, null = True , blank = True, verbose_name=_('address_details'))
    phone = models.CharField(max_length=20, null=True,
                             blank=True, verbose_name=_('phone'))
    work_time = models.CharField(
        max_length=70, blank=True, default='Mon to Fri 9am to 6 pm', verbose_name=_('work_time'))
    email               = models.EmailField(max_length=200, null = True , blank = True, verbose_name=_('email'))
    Send_any_time = models.CharField(
        max_length=70, blank=True, default='Send us your query anytime!', verbose_name=_('Send_any_time'))
        
    class Meta:
        verbose_name_plural = _('ContactInfo')
    
    def __str__(self):
        return self.phone + "-" + self.email



class MenuBarEn(models.Model):
     menu = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name=_('name'))
     url = models.CharField(max_length=100, null=True, blank=True,
                           default='/', help_text="eg: /page", verbose_name=_('url'))

     class Meta:
        verbose_name_plural = _('MenuBar En')

     def __str__(self) -> str:
        return self.menu

class MenuBarAr(models.Model):
     menu = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name=_('name'))
     url = models.CharField(max_length=100, null=True, blank=True,
                           default='/', help_text="eg: /page", verbose_name=_('url'))

     class Meta:
        verbose_name_plural = _('MenuBar Ar')

     def __str__(self) -> str:
        return self.menu
    