from django.shortcuts import render
from categorias.models import Categoria
from django.views.generic import ListView
from django.views import generic
from categorias.forms import CategoriaCreateForm

# class CategoriaListView(ListView):
#     model = Categoria
#     context_object_name = 'categorias'
#     template_name = 'categorias/categorias.html'
# Create your views here.

# class ListPostsView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'posts/listposts.html'
#     ordering = ['-created_at',]
class CategoriaCreateView(generic.CreateView):
        model = Categoria
        context_object_name = 'categorias'
        form_class = CategoriaCreateForm
        template_name = 'categorias/categorias.html'
        


# class PostUpdateView(generic.UpdateView):
#     model = Post
#     fields = ['autor', 'conteudo',] 
#     template_name = 'posts/edit.html'
#     success_url = reverse_lazy('posts:ListPosts')

# class PostDeleteView(generic.DeleteView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'posts/delete.html'
#     success_url = reverse_lazy('posts:ListPosts')