from django.urls import path
from comentarios.views import ComentarioCreateView,ComentarioUpdateView,ComentarioDeleteView,ComentarioListView
app_name = 'comentarios'

urlpatterns = [
    path('comentarios',ComentarioCreateView.as_view(),name='CriaComentarios'),
    path('listcomentarios',ComentarioListView.as_view(),name='ListaComentarios'),
    path('comentarios/<int:pk>/edit',ComentarioUpdateView.as_view(),name='editaComentarios'),
    path('comentarios/<int:pk>/delete',ComentarioDeleteView.as_view(),name='deletaComentarios'),
] 

