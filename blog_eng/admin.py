from dataclasses import fields
from django.contrib import admin
from project.settings import LANGUAGE_CODE, LANGUAGES
from .models import AdsWidget, Blog,  AboutAuthor,   NameWidget,  Comment
# Register your models here.

admin.site.site_header = 'Ahmed Fathy'
admin.site.site_title = 'dashboard'





#class InlineCategory(admin.StackedInline):
   # model = Category
   # extra = 1
   
   


#class BoardAdmin(admin.ModelAdmin):
   # inlines = [InlineCategory]





admin.site.register(Blog)


admin.site.register(AboutAuthor)
admin.site.register(NameWidget)
admin.site.register(AdsWidget)
admin.site.register(Comment)
