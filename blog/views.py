from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def contact(request):
    return render(request, 'contact.html')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPost(generic.CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'
