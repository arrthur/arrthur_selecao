# -*- coding: utf-8 -*-
from django import forms
from categoria.models.categoria import Categoria


class CategoriaForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):         
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = "form-control"
        
        
    class Meta():
        model = Categoria
        fields = '__all__' 
    
    