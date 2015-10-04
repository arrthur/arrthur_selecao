# -*- coding: utf-8 -*-
from django import forms
from item.models.item import Item


class ItemForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):         
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = "form-control"
        self.fields['valor'].widget.attrs['class'] = "form-control"
        self.fields['tempo_preparo'].widget.attrs['class'] = "form-control"
        self.fields['ingrediente'].widget.attrs['class'] = "form-control"
        self.fields['categoria'].widget.attrs['class'] = "form-control"
        
        
        
    class Meta():
        model = Item
        fields = '__all__' 
    
    