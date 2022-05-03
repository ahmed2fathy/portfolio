from dataclasses import fields
from urllib import request

from django.conf import settings

from django.contrib import admin

from project.settings import LANGUAGE_CODE, LANGUAGES
from .models import  AdsWidget, Blog, Category, AboutAuthor, MenuBar, NameWidget, Tag , Comment
# Register your models here.

admin.site.site_header = 'Ahmed Fathy'
admin.site.site_title = 'dashboard'




class BlogAdmin(admin.ModelAdmin):
     
    

    #fields = ('title', 'title_ar', 'author','category', 'tag', 'created_at',)
   
       fields = ('title_en', 'content_en', 'title_ar', 'content_ar', 'image', 'created_at',
                 'author', 'category', 'tag', 'views', 'slug')
       list_display = ('title_en', 'title_ar',
                        'author', 'category', 'tag', 'created_at',)
       list_display_link = ('title_en' and 'title_ar', 'author', )
       search_fields = ('title_en''title_ar',)
       list_editable = ('category', 'tag', 'created_at',)
       list_filter = ('author', 'category', 'created_at')
       date_hierarchy = ('created_at')
     
  

         
        
   
   
    
#class InlineCategory(admin.StackedInline):
   # model = Category
   # extra = 1


#class BoardAdmin(admin.ModelAdmin):
   # inlines = [InlineCategory]




admin.site.register(MenuBar)
admin.site.register(Tag )
admin.site.register(Category )
admin.site.register(Blog, BlogAdmin,)
admin.site.register(AboutAuthor)
admin.site.register(NameWidget)
admin.site.register(AdsWidget)
admin.site.register(Comment)




