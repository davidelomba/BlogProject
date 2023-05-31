from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post, Category


# Create your views here.


class PostList(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    cats = Category.objects.all()
    ordering = ['created_on']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        print(cat_menu)
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        print(cat_menu)
        return context


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'content', 'slug']


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


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


class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_post': category_post})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})
