from dataclasses import fields
from django.contrib import admin
from project.settings import LANGUAGE_CODE, LANGUAGES
from .models import AdsWidget, Blogs,  AboutAuthor, Category,  NameWidget,  Comment, Tag
# Register your models here.

admin.site.site_header = 'Ahmed Fathy'
admin.site.site_title = 'dashboard'


class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'image', 'created_at',
              'author_ar',  'views', 'slug')
    list_display = ('title', 
                    'author_ar',   'created_at',)
    list_display_link = (
        'title',  'author_ar', )
    search_fields = ('title', 'content',)
    list_editable = ('created_at',)
    list_filter = ('author_ar', 'created_at')
    date_hierarchy = ('created_at')


#class InlineCategory(admin.StackedInline):
   # model = Category
   # extra = 1


#class BoardAdmin(admin.ModelAdmin):
   # inlines = [InlineCategory]





admin.site.register(Blogs, BlogAdmin,)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(AboutAuthor)
admin.site.register(NameWidget)
admin.site.register(AdsWidget)
admin.site.register(Comment)
