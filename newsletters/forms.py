from django import forms
from django.forms import fields
from . models import NewsletterUser


class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields =['email']
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email