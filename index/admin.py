from django.contrib import admin
from .models import Brand, Call, ClientSay, ClientSay, FooterHeader, Hello, MySelf, NewsletterUser, Service, Tab, Work


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'data_added',)
    
    
admin.site.register(NewsletterUser,NewsletterAdmin)


# Register your models here.
admin.site.register(Hello)
admin.site.register(Call)
admin.site.register(Brand)
admin.site.register(ClientSay)
admin.site.register(MySelf)
admin.site.register(Service)
admin.site.register(Work)
admin.site.register(FooterHeader)
admin.site.register(Tab)