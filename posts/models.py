from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey("users.User",verbose_name=('autor'), related_name='PostsFromAuthor', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()
    categoria = models.ForeignKey("categorias.Categoria",verbose_name=('Categoria'),on_delete=models.CASCADE)
    imagem = models.ImageField(verbose_name='Imagem', blank = True, upload_to= 'posts')
 
    def __str__(self):
        return f'Post {self.pk} | Author {self.autor} | Created at {self.created_at}'

    class Meta:
     verbose_name ='Postagem'
     verbose_name_plural = 'Postagens'