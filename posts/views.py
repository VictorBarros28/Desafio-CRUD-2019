from django.shortcuts import render, get_object_or_404
from posts.models import Post
from django.views.generic import ListView,CreateView,DeleteView
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListPostsView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/listposts.html'
    ordering = ['-created_at',]

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/criaposts.html'
    success_url = reverse_lazy('posts:ListPosts')


class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Post
    fields = ['autor', 'conteudo','categoria'] 
    template_name = 'posts/edit.html'
    success_url = reverse_lazy('posts:ListPosts')

class PostDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:ListPosts')

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/detail.html'
