from django.contrib import admin
from .models import  AdsWidget, Blog, Category, AboutAuthor, MenuBar, NameWidget, Tag , Comment
# Register your models here.

admin.site.site_header = 'Ahmed Fathy'
admin.site.site_title = 'dashboard'


admin.site.register(MenuBar)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(AboutAuthor)
admin.site.register(NameWidget)
admin.site.register(AdsWidget)
admin.site.register(Comment)




