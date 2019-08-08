from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from django.urls import reverse_lazy 
from comentarios.forms import ComentarioCreateForm
from comentarios.models import Comentario
# Create your views here.


class ComentarioListView(ListView):
    model = Comentario
    context_object_name = 'listcomentarios'
    template_name = 'comentarios/listcomentarios.html'
    

class ComentarioCreateView(generic.CreateView):
        model = Comentario
        context_object_name = 'comentarios'
        form_class = ComentarioCreateForm
        template_name = 'comentarios/comentarios.html'
        success_url = reverse_lazy('posts:ListPosts')
        


class ComentarioUpdateView(generic.UpdateView):
    model = Comentario
    fields = ['comentario'] 
    template_name = 'comentarios/edit.html'
    success_url = reverse_lazy('comentarios:ListaComentarios')

class ComentarioDeleteView(generic.DeleteView):
    model = Comentario
    context_object_name = 'comentarios'
    template_name = 'comentarios/delete.html'
    success_url = reverse_lazy('comentarios:ListaComentarios')