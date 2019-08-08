from django import forms
from comentarios.models import Comentario

class ComentarioCreateForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario', 'post']