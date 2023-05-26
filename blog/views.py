from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import PostForm
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


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'slug']


def add_post(request):
    submitted = False

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = PostForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_post.html', {'form': form, 'submitted': submitted})
