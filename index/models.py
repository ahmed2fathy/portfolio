from django.db import models
from  django.utils import timezone
# Create your models here.

class NewsletterUser(models.Model):
    email= models.EmailField()
    data_added= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email


class FooterHeader(models.Model):
    site_name           = models.CharField(max_length = 220)
    logo                = models.ImageField (upload_to = 'media/index/FollowMe/',null = True , blank = True)
    phone               = models.CharField(max_length = 20, null = True , blank = True)
    address             = models.CharField(max_length = 300, null = True , blank = True)
    email               = models.EmailField(max_length = 254, null = True , blank = True)
    description         = models.TextField(max_length = 500, null = True , blank = True)
    follow_me_text_name = models.CharField(max_length = 220, null = True , blank = True, default='FOLLOW ME')
    fb_link             = models.URLField(max_length = 400,  null = True , blank = True)
    twitter_link        = models.URLField(max_length = 400, null = True , blank = True )
    instagram_link      = models.URLField(max_length = 400,  null = True , blank = True)
    Copyright           = models.CharField(max_length = 220, null = True , blank = True, default='Copyright')
    all_rights_reserved = models.CharField(max_length = 220, null = True , blank = True,default=' All rights reserved')
    Copyright_txt_1     = models.CharField(max_length = 220, null = True , blank = True, default='This template is made with')
    Copyright_txt_2     = models.CharField(max_length = 220, null = True , blank = True,default='by')
    Copyright_link      = models.URLField(max_length = 400, null = True , blank = True )
    Copyright_date      = models.DateTimeField(default = timezone.now)
    
    def  __str__(self):
            return self.site_name
    

class Hello(models.Model):
    hello_name = models.CharField(max_length=50,  default='hello')
    title = models.CharField(max_length=50 , blank = True)
    des = models.TextField(max_length=400 , blank = True)
    image_banner = models.ImageField(upload_to='media/index/hello/' ,null = True , blank = True)
    cv = models.CharField(max_length=50,  default='Get CV')
    cv_link = models.URLField(max_length = 2000, null = True , blank = True )
    hire = models.CharField(max_length=50,  default='Hire Me')
    hire_link = models.URLField(max_length = 2000, null = True , blank = True )
    back_banner = models.ImageField(upload_to='media/index/hello/' ,null = True , blank = True)
    phone = models.CharField(max_length=50, blank = True)
    
    def __str__(self):
            return self.hello_name
        
        
        
class MySelf(models.Model):
    title= models.CharField(max_length=50)
    des= models.TextField(max_length=400, blank = True )
    download_cv = models.CharField(max_length=50,  default=' Download CV')
    download_link = models.URLField(max_length = 2000, null = True , blank = True )
    image = models.ImageField(upload_to='media/index/myself/', null = True , blank = True)
    
    def __str__(self) -> str:
        return self.title



class Call(models.Model):
    title = models.CharField(max_length=50,default='call us now',)
    des = models.TextField(max_length=400,  null = True , blank = True)
    image = models.ImageField(upload_to='media/index/call/' , null = True , blank = True)
    phone = models.CharField(max_length=50, null = True , blank = True )
    experience =models.CharField(max_length=60,default=' Years Experience Working', null = True , blank = True) 
    years = models.IntegerField(default='3', null = True , blank = True)
   
    def __str__(self) -> str:
        return self.title
        
        
     
class Service(models.Model):
    big_name = models.CharField(max_length=50, null = True , blank = True)
    big_dec = models.TextField(max_length=300, null = True , blank = True)
    title= models.CharField(max_length=50)
    des= models.TextField(max_length=400)
    image = models.ImageField(upload_to='media/index/service/')
    
    def __str__(self) -> str:
        return self.title
        
        

class Work(models.Model):
    
    title = models.CharField(max_length=50,)
    des = models.TextField(max_length=300, null = True , blank = True)
    def __str__(self) -> str:
            return self.title
            
    
class Tab(models.Model):
    status_tab= [
    ('Popular','Popular'),
    ('Latest','Latest'),
    ('Following','Following'),
    ('Upcoming','Upcoming'),
    ]
    status = models.CharField(max_length=50 , choices=status_tab, null=True, blank = True)
    title = models.CharField(max_length=50, null = True , blank = True)
    des = models.TextField(max_length=300, null = True , blank = True)
    image = models.ImageField(upload_to='media/index/work/popular/' ,null = True , blank = True)
    active = models.BooleanField(default= True)
    def __str__(self) -> str:
            return self.title

        
        
class ClientSay(models.Model):
    big_name = models.CharField(max_length=50, null = True , blank = True)
    big_dec = models.TextField(max_length=300, null = True , blank = True)
    title= models.CharField(max_length=60)
    des= models.TextField(max_length=400)
    image = models.ImageField(upload_to='media/index/clientsay/')
    
    def __str__(self) -> str:
        return self.title
     
            
class Brand(models.Model):
    image= models.ImageField(upload_to='media/index/brands/', null = True , blank = True)
    def __str__(self) -> str:
            return str (self.image)
     
    
    
    
    

    