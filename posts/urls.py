from django.urls import path
from posts.views import ListPostsView, PostCreateView,PostUpdateView,PostDeleteView
app_name = 'posts'

urlpatterns = [
    path('posts',ListPostsView.as_view(),name='ListPosts'),
    path('criacao',PostCreateView.as_view(),name='CriaPosts'),
    path('posts/<int:pk>/alterar',PostUpdateView.as_view(),name='atualizaPosts'),
    path('posts/<int:pk>/deletar',PostDeleteView.as_view(),name='deletaPosts'),
] 