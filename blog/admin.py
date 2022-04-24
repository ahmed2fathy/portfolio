from dataclasses import fields
from django.contrib import admin
from .models import  AdsWidget, Blog, Category, AboutAuthor, MenuBar, NameWidget, Tag , Comment
# Register your models here.

admin.site.site_header = 'Ahmed Fathy'
admin.site.site_title = 'dashboard'




class BlogAdmin(admin.ModelAdmin):
    #fields = ('title', 'title_ar', 'author','category', 'tag', 'created_at',)
    list_display = ('title', 'title_ar',
                    'author', 'category', 'tag', 'created_at',)
    list_display_link = ('title', 'author', )
    list_editable = ( 'title_ar','category', 'tag', 'created_at',)
    list_filter = ('author', 'category', 'created_at')
    search_fields = ('title', 'title_ar',)
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




