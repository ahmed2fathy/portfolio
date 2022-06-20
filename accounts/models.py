
# -*- coding: UTF-8 -*-

from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.





class Profile(models.Model):
    gender = (
        ('Male', 'Male'),
        ('Fmale', 'Fmale'),

    )
    user = models.ForeignKey(User, related_name='user_profile',
                             on_delete=models.CASCADE, default='User')
    image = models.ImageField(
        upload_to='profile/', blank=True, null=True, )
    phone_number = models.CharField(max_length=20 , blank=True, null=True)
    address             = models.CharField(max_length = 300, null = True , blank = True)
    email = models.EmailField(max_length=254, null=True, blank=True, default='User.email')
    description         = models.TextField(max_length = 300, null = True , blank = True, verbose_name='About')
    skills = models.CharField(max_length=300, null=True, blank=True, default='PHP, HTML, CSS, JavaScript, JQuery')
    gender = models.CharField(max_length=40, blank=True, null=True, choices=gender)
    country = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    fb_link             = models.URLField(max_length = 400,  null = True , blank = True)
    twitter_link        = models.URLField(max_length = 400, null = True , blank = True )
    instagram_link      = models.URLField(max_length = 400,  null = True , blank = True)


    def __str__(self):
        return str(self.user)

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)