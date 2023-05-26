from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Enter the title',
            'slug': 'Enter the slug',
            'author': 'Enter the author',
            'content': 'Enter the content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
