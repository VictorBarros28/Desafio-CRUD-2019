from django.shortcuts import render
from categorias.models import Categoria
from django.views.generic import ListView
from django.views import generic
from categorias.forms import CategoriaCreateForm
from django.urls import reverse_lazy 

class CategoriaListView(ListView):
    model = Categoria
    context_object_name = 'listcategorias'
    template_name = 'categorias/listCategorias.html'
    ordering = ['-created_at',]

class CategoriaCreateView(generic.CreateView):
        model = Categoria
        context_object_name = 'categorias'
        form_class = CategoriaCreateForm
        template_name = 'categorias/categorias.html'
        success_url = reverse_lazy('posts:CriaPosts')
        


class CategoriaUpdateView(generic.UpdateView):
    model = Categoria
    fields = ['categoria'] 
    template_name = 'categorias/edit.html'
    success_url = reverse_lazy('posts:ListPosts')

class  CategoriaDeleteView(generic.DeleteView):
    model = Categoria
    context_object_name = 'categorias'
    template_name = 'categorias/delete.html'
    success_url = reverse_lazy('posts:ListPosts')