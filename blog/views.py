from django.shortcuts import render
from .models import Post


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def contact(request):
    return render(request, 'contact.html')
