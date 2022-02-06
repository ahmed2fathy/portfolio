
from pyexpat import model
from unicodedata import category
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
import index




# Create your models here.

class Tag(models.Model):
    name= models.CharField(max_length=80,  default='Enter tag name ')
    des   = models.TextField(max_length=40, null = True, blank = True)
    image =  image =  models.ImageField( upload_to='media/blog/frontbage/tag', null = True, blank = True)
    slug = models.SlugField(null = True, blank = True)
    
    def __str__(self) -> str:
        return self.name
        
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify (self.name)
         
        super(Tag, self).save(*args, **kwargs) # Call the real save() method
        
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:single_blog', kwargs={'slug': self.slug})    
        
    
    
class Category(models.Model):
    name= models.CharField(max_length=80 , default='Enter category name ')
    des   = models.TextField(max_length=40, null = True, blank = True)
    image =  image =  models.ImageField( upload_to='media/blog/frontbage/category', null = True, blank = True)
    slug = models.SlugField(null = True, blank = True)
    
    
    def __str__(self) -> str:
        return self.name
        
        
        



class  Blog(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField(max_length=4000)
    image =  models.ImageField( upload_to='media/blog/frontbage')
    created_at = models.DateTimeField(default= timezone.now)
    author =  models.ForeignKey(User , related_name ='post_author',default=User, on_delete = models.CASCADE)
    category = models.ForeignKey('Category', related_name='post_category',default=Category, on_delete = models.CASCADE )
    tag = models.ForeignKey('Tag', related_name='post_tag', default=Tag, on_delete = models.CASCADE)
    views = models.IntegerField(default=0)
    slug = models.SlugField(null = True, blank = True)
    
    
    class Meta:
        ordering = ["-created_at", "title"]
        
    
    def __str__(self) -> str:
        return self.title
        
    def total_views(self):
            return self.views.count()

        
        
        
     # دالة تحويل اسم المقال الي رابط وازالة المسافات الفارغة ووضع - داش 
    
    def save(self, *args, **kwargs):
        from django.utils.text import slugify
        if not self.slug:
            self.slug = slugify (self.title)
         
        super(Blog, self).save(*args, **kwargs) # Call the real save() method
        
    #-----------------------------------------------------------------------------
    
  
     # دالة جلب رابط المقال
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog:single_blog', kwargs={'slug': self.slug})
        
    #--------------------------------------------------------
    
    
class AboutAuthor(models.Model):
    image = models.ImageField(upload_to='media/blog/frontbage/about')
    name = models.CharField(max_length=70,default='user')
    short_des = models.CharField(max_length=70, default='Senior blog writer')
    des   = models.TextField(max_length=300)
    fb_link = models.URLField( max_length=300, null = True , blank = True)
    twitter_link = models.URLField( max_length=300, null = True , blank = True)
    github_link = models.URLField( max_length=300, null = True , blank = True)
    
    def __str__(self) -> str:
        return self.name
    
    
class NameWidget(models.Model):
    popular_post = models.CharField(max_length=90, default='Popular Posts')
    post_catgories = models.CharField(max_length=90, default='Post Catgories')
    newsletter = models.CharField(max_length=90, default='Newsletter')
    tag_clouds = models.CharField(max_length=90, default='Tag Clouds')
    
    
    def __str__(self) -> str:
        return str('wedgit')
        
        
        
class AdsWidget(models.Model):
    ad_code_1 = models.TextField(null = True , blank = True , default='Enter ads code')
    ad_code_2 = models.TextField(null = True , blank = True, default='Enter ads code')
    ad_code_3 = models.TextField(null = True , blank = True ,default='Enter ads code')
    ad_code_4 = models.TextField(null = True , blank = True, default='Enter ads code')
    ad_code_5 = models.TextField(null = True , blank = True,default='Enter ads code')
    ad_code_6 = models.TextField(null = True , blank = True, default='Enter ads code')
    
    def __str__(self) -> str:
        return str('ad')
    

class Comment(models.Model):
    post = models.ForeignKey(
        Blog, related_name='Comments', on_delete=models.CASCADE, default='self')
    name = models.CharField(max_length=70)
    email = models.EmailField()
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

        



class MenuBar(models.Model):
    menu = models.CharField(max_length=100, null=True, blank=True,)
    url = models.URLField(null = True , blank = True,)
    
    def __str__(self) -> str:
        return self.menu
   
    
    
        

        
        
        
        

    
