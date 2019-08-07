from django.urls import path
from categorias.views import CategoriaCreateView
app_name = 'categorias'

urlpatterns = [
    path('categorias',CategoriaCreateView.as_view(),name='CriaCategorias'),
    
] 