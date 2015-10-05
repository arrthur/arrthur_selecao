from rest_framework import serializers
from categoria import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Categoria
        fields = ('id', 'nome')
        