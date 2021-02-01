from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"contexts": posts})


def about(request):
   return render(request, "blog/about.html") 
