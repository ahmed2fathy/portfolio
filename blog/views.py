from django.shortcuts import render
from .models import *
# Create your views here.
 
def  blog(request):
    all_blogs = Blog.objects.all()
    
    context ={
    
    'all_blogs': all_blogs,
    
    }
    
    return render(request,'pages/blog.html', context)
