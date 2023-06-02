from django import forms
from django.forms import ModelForm
from .models import *

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'content', 'snippet', 'status')
        labels = {
            'title': 'Enter the title',
            'slug': 'Enter the slug',
            'author': 'Enter the author',
            'content': 'Enter the content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }


class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'slug', 'snippet', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

        }
