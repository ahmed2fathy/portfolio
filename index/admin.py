from django.contrib import admin

from accounts import models
from project.settings import LANGUAGE_CODE, LANGUAGES
from .models import MenuBarAr, MenuBarEn, Skills, Call, ClientSay, ClientSay, ContactInfo, Feedback,  FooterHeader, Hello, MySelf, NewsletterUser, Service, Tab, Work


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_added',)
    
    
admin.site.register(NewsletterUser,NewsletterAdmin)


# Register your models here.
admin.site.register(Hello)
admin.site.register(Call)
admin.site.register(Skills)
admin.site.register(ClientSay)
admin.site.register(MySelf)
admin.site.register(Service)
admin.site.register(Work)
admin.site.register(FooterHeader)
admin.site.register(Tab)
admin.site.register(Feedback, FeedbackAdmin, )
admin.site.register(ContactInfo)
admin.site.register(MenuBarEn)
admin.site.register(MenuBarAr)







