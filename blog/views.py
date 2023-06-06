from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .forms import PostForm, EditForm, CommentForm
from .models import Post, Category, Comment


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
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class UpdatePost(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


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


def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


def add_comment(request, pk):
    eachComment = Post.objects.get(id=pk)

    form = CommentForm(instance=eachComment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=eachComment)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['body']

            c = Comment(post=eachComment, name=name, body=body, date_added=datetime.now())
            c.save()
            return redirect('home')
        else:
            print('form is invalid')
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'add_comment.html', context)
