from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    email= models.EmailField()
    data_added= models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email