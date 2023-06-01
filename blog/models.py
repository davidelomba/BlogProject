from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class NameField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.CharField(max_length=200, default='Uncategorized')
    snippet = models.CharField(max_length=200, default='Click Link Above to Read Blog Post')
    likes = models.ManyToManyField(User, related_name="blog_post")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
