# -*- coding: utf-8 -*-
from django import forms
from ingrediente.models.ingrediente import Ingrediente


class IngredienteForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):         
        super(IngredienteForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = "form-control"
        
        
    class Meta():
        model = Ingrediente
        fields = '__all__' 
    
    