from django import forms
from categorias.models import Categoria

class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['categoria']