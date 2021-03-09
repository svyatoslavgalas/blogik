from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView)
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)

from .models import Post


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['name', 'content', 'cover']
    success_url = reverse_lazy('post:list')


class PostUpdate(UpdateView):
    model = Post
    fields = ['name', 'content', 'cover']


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post:list')

