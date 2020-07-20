from django.shortcuts import render
from .models import Blog
# Create your views here.

def layout(request):
    blogs = Blog.objects
    return render(request,'myapp/layout.html', {'blogs':blogs})
