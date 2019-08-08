from django.urls import path
from categorias.views import CategoriaCreateView,CategoriaUpdateView,CategoriaDeleteView,CategoriaListView
app_name = 'categorias'

urlpatterns = [
    path('categorias',CategoriaCreateView.as_view(),name='CriaCategorias'),
    path('listCategorias',CategoriaListView.as_view(),name='ListaCategorias'),
    path('categorias/<int:pk>/edit',CategoriaUpdateView.as_view(),name='editaCategorias'),
    path('categorias/<int:pk>/delete',CategoriaDeleteView.as_view(),name='deletaCategorias'),
] 