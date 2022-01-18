from django.contrib import admin
from .models import  AdsWidget, Blog, Category, AboutAuthor, Comment, NameWidget, Tag
# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(AboutAuthor)
admin.site.register(NameWidget)
admin.site.register(AdsWidget)
admin.site.register(Comment)


