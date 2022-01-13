from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    pass
    
    
class Category(models.Model):
    pass


class  Blog(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField(max_length=4000)
    image =  models.ImageField( upload_to='media/blog/frontbage')
    create_at = models.DateTimeField(default= timezone.now)
    author =  models.ForeignKey(User , related_name ='post_author',on_delete = models.CASCADE)
    category = models.ForeignKey('Category', related_name='post_category', on_delete = models.CASCADE )
    tag = models.ForeignKey('Tag', related_name='post_tag', on_delete = models.CASCADE)
    slug = models.SlugField(null = True, blank = True)
    def __str__(self) -> str:
        return self.title
        
        

    
