from django.db import models

# Create your models here.
class Comentario(models.Model):
    comentario = models.TextField()
    post = models.ForeignKey("posts.Post",verbose_name=('Post:'),on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.comentario}'